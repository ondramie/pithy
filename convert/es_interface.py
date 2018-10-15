#!/usr/bin/python3

"""Elasticsearch interface for error codes in debugger"""

import json     	                                        # json.dumps()
import sys			                                        # sys.argv()
from elasticsearch import Elasticsearch                     # ES object
from elasticsearch_dsl import Search, Q
from elasticsearch_dsl.query import MultiMatch, Match, MoreLikeThis
from pprint import pprint
from Timer import MyTimer                                   # class to record elapsed time
from my_ips import private_ips                              # contains ips for AWS instances


def print_results(results, index, qtime):
    print("START")
    print("Results %d in index %s took %.6g"%(results['hits']['total'], index, qtime))
    pprint(results['hits']['hits'][0]['_source'])
    print("END")

def search(es, ft_query, index, field, text, size):
    #print("The " + ft_query + ":" )
    return es.search(index=index, 
                        size=size, 
                            doc_type=index, 
                                body={
                                    "query": {
                                            ft_query: {field: text}
                                    }
                    })

def answer(es, res, index):
    # A post can be a question or answer. An accepted question has an AcceptedAnswerId
    # A de-facto answer references its ParentId and has the highest score.ß 
    ParentId = res['hits']['hits'][0]['_source']["ParentId"]                    # question
    AcceptedAnswerId = res['hits']['hits'][0]['_source']["AcceptedAnswerId"]    # answer
    if AcceptedAnswerId != None:
        top_answer = search(es, "term", index, "Id", AcceptedAnswerId, 1)['hits']['hits'][0]['_source']['Body']
    elif AcceptedAnswerId == None and ParentId != None:
        # Not an accepted answer but get the top answer
        answers = search(es, "term", index, "ParentId", ParentId, 10)
        max_score = 0
        for answer in answers['hits']['hits']:
            if max_score < answer['_source']['_score']:
                max_score = answer['_source']['_score']
                top_answer = answer['_source']['Body']
    else: 
        # No change; NOTE: remove when optimized 
        top_answer = res['hits']['hits'][0]['_source']['Body']

    return top_answer 


def main(myError):     
    es = Elasticsearch(private_ips())                           # establishes client
    index = 'posts2'                                            # index to query ES 
    query_type = "match"
    res = search(es, query_type, index, "Body", myError, 1)

    #s = Search(using=es, index=index).query("match", Body=myError)
    #response = s.execute()
    #pprint(response[0]['ParentId'])
    
    if len(res) > 0:
        pprint(answer(es, res, index))

if __name__  == "__main__":
    #print(sys.argv)
    main(sys.argv[1])