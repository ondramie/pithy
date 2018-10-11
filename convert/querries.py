#!/usr/bin/python3

''' Sample queries of error codes'''

import json     	                                        # json.dumps()
import sys			                                        # sys.argv()
from elasticsearch import Elasticsearch                     # ES object
from elasticsearch_dsl import Search, Q
from elasticsearch_dsl.query import MultiMatch, Match
from pprint import pprint
from runtime_errors import StackErrors                      # errors used for benchmark 
from Timer import MyTimer                                   # class to record elapsed time


def print_results(qtype, results, index, qtime):
    print("Results %d in index %s took %.6g"%(results['hits']['total'], index, qtime))
    pprint(results['hits']['hits'])
    print("END")

def searches(es, ft_query, index, field, text):
    print("The " + ft_query + ":" )
    return es.search(index=index, size=2, doc_type=index, body={"query": {ft_query: {field: text}}})

def main(): 
    # pulsing EC2 cluster name: ES-2     
    es = Elasticsearch(['18.234.204.121:9200',
                        '54.209.55.117:9200',
                        '54.88.62.138:9200',
                        '54.210.232.252:9200'])
    
    #for index in ["postlinks", "posts"]: 
    index = 'posts'
    myError = StackErrors()

    with open("search_results.csv") as ouput: 
        # Query gives format of the index
        doc = {'size': 1, 'query': { 'match_all': {}}}
        mytimer = MyTimer()
        res = es.search(index=index, doc_type=index, body=doc)      
        print_results('none', res, index, mytimer.end())
        
        '''Full-text queries'''
        # "match" query for performing full text queries, including fuzzy matching 
        # and phrase or proximity queries. 
        mytimer = MyTimer()
        query_type = "match"
        res = searches(es, query_type, index, "Body", myError.large_trace_nofolders)
        print_results(query_type, res, index, mytimer.end())

        # Like match query but used for matching exact phrases or word proximity matches.
        mytimer = MyTimer()
        query_type = "match_phrase"
        res = searches(es, "match_phrase", index, "Body", myError.large_trace_nofolders)
        print_results(query_type, res, index, mytimer.end())

        # "match" query with fuziness 
        mytimer = MyTimer()
        res = es.search(index=index, 
                        size=2, 
                            doc_type=index, 
                                body= {"query": {
                                        "match": {
                                            "Body" : {
                                                "query" : myError.large_trace_folders,
                                                "operator": "and"
                                            }
                                        }
                                    }
                                })
        print_results("match", res, index, mytimer.end())
    
    # TODO: More like this Query
    #links = [entries['_source']['_source']['Id'] for entries in res['hits']['hits']]
    # websites
    #sites = ["https://stackoverflow.com/questions/" + str(link) for link in links]
    #print(sites)

if __name__  == "__main__":
    main()