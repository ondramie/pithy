#!/usr/bin/python3

'''Queries elasticsearch for error codes. This forms basis for comparison and 
downselects the best query answer for analysis'''

import json     	                                        # json.dumps()
import sys			                                        # sys.argv()
from elasticsearch import Elasticsearch                     # ES object
from elasticsearch_dsl import Search, Q
from elasticsearch_dsl.query import MultiMatch, Match, MoreLikeThis
from pprint import pprint
from runtime_errors import StackErrors                      # errors used for benchmark 
from Timer import MyTimer                                   # class to record elapsed time
from my_ips import private_ips                              # contains ips for AWS instances


def print_results(results, index, qtime):
    pprint("START")
    print("Results %d in index %s took %.6g"%(results['hits']['total'], index, qtime))
    pprint(results['hits']['hits'][0]['_source'])
    print("END")

def searches(es, ft_query, index, field, text, size):
    #print("The " + ft_query + ":" )
    return es.search(index=index, 
                        size=size, 
                            doc_type=index, 
                                body={
                                    "query": {ft_query: {field: text}
                                }
                            })

def write_file(objects, index, query, name, times, success): 
    objects.write("%s,\t%s,\t%s,\t%s\t%s,\n"%(index, query, name, times, success))

def find_answer(es, res, index):
    # A post can be a question or answer. An accepted question has an AcceptedAnswerId
    # A de-facto answer references its ParentId and has the highest score. 
    ParentId = res['hits']['hits'][0]['_source']["ParentId"]                    # question
    AcceptedAnswerId = res['hits']['hits'][0]['_source']["AcceptedAnswerId"]    # answer
    
    if AcceptedAnswerId != None:
        top_answer = searches(es, "term", index, "Id", AcceptedAnswerId, 1)['hits']['hits'][0]['_source']['Body']
    elif AcceptedAnswerId == None and ParentId != None:
        answers = searches(es, "term", index, "ParentId", ParentId, 10)
        max_score = 0
        # no accepted answer but get the top answer
        for answer in answers['hits']['hits']:
            if max_score < answer['_source']['_score']:
                max_score = answer['_source']['_score']
                top_answer = answer['_source']['Body']
    return top_answer

def main():     
    es = Elasticsearch(private_ips(), )                           # establishes client
    index = 'posts2'                                            # index to query ES 
    myError = StackErrors().long_st                             # error under investigation
    type_error = "Long Trace"
    print(type_error)

    for _ in range(1000):
        with open("search_results.csv", "a") as output: 
            # "match" query for performing full text queries, including fuzzy matching 
            # and phrase or proximity queries.  The results are an array of dictionaries. 
            mytimer = MyTimer()
            query_type = "match"
            res = searches(es, query_type, index, "Body", myError, 1)
            #print_results(res, index, mytimer.get_end())
        
            if len(res) > 0:
                #pprint(find_answer(es, res, index))
                write_file(output, index, query_type, type_error, mytimer.get_end(), 1)
            else:
                write_file(output, index, query_type, type_error, mytimer.get_end(), 0)
            
            # Like match query but used for matching exact phrases or word proximity matches.
            query_type = "match_phrase"
            for analyzer in ["simple", "standard", "stop"]:
                mytimer = MyTimer()
                res = es.search(index=index, 
                                size=1, 
                                    doc_type=index, 
                                        body={
                                            "query": {
                                                "match_phrase": {
                                                    "Body" : {
                                                        "query" : myError,
                                                        "analyzer": analyzer 
                                                    }
                                                }
                                            }
                                }, request_timeout=180)
                #print_results(res, index, mytimer.get_end())
                if len(res) > 0:
                    #pprint(find_answer(es, res, index))
                    write_file(output, index, query_type + analyzer, type_error, mytimer.get_end(), 1)
                else:
                    write_file(output, index, query_type + analyzer, type_error, mytimer.get_end(), 0)

            # "match" query with fuziness 
            mytimer = MyTimer()
            query_type = "match + fuzzy"
            res = es.search(index=index, 
                            size=1, 
                                doc_type=index, 
                                    body={"query": {
                                            "match": {
                                                "Body" : {
                                                    "query" : myError,
                                                    "operator": "or", 
                                                    "zero_terms_query": "all"
                                                }
                                            }
                                        }
                            }, request_timeout=180)
            #print_results(res, index, mytimer.get_end())
            if len(res) > 0:
                #pprint(find_answer(es, res, index))
                write_file(output, index, query_type, type_error, mytimer.get_end(), 1)
            else:
                write_file(output, index, query_type, type_error, mytimer.get_end(), 0)
            
            # "More like this Query" 
            mytimer = MyTimer()
            query_type = "more like this"

            res = es.search(index=index,  
                                    doc_type=index, 
                                        body={"query": {
                                            "more_like_this" : {
                                                "fields" : ["Body"],
                                                    "like" : myError,
                                                    "min_term_freq" : 1,
                                                    "max_query_terms" : 12
                                                }
                                            }
                            }, request_timeout=180)
            if len(res) > 0:
                #pprint(find_answer(es, res, index))
                write_file(output, index, query_type, type_error, mytimer.get_end(), 1)
            else:
                write_file(output, index, query_type, type_error, mytimer.get_end(), 0)

if __name__  == "__main__":
    main()