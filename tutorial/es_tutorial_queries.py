#!/usr/bin/python3

''' Sample queries from index = "shakespaeare"
'''

import json     	                                # json.dumps()
import sys			                                # sys.argv()
from elasticsearch import Elasticsearch, helpers    # helpers.bulk()

def main():     
    es = Elasticsearch()
    index="shakespeare"
    doc="doc"

    # searches for speaker WESTMORELAND
    res = es.search(index=index, doc_type=doc, 
        body={"query": {"match": {"speaker": "WESTMORELAND"}}})
    print("match")
    print(json.dumps(res, indent=2))
    print("========================")

    # gets id == 1
    '''res = es.get(index=index, doc_type=doc, id=1)
    print("get")
    print(res['_source'])
    print("========================")'''

    # checks if index exits
    res = es.indices.exists(index=index)
    print("exists")
    print(res)
    print("========================")

    # 
    res = es.search(index=index, doc_type=doc, 
        body={"size": 2, "query": {"match_phrase": {"speaker": "*MORE"}}})
    print("match_phrase")
    print(json.dumps(res))
    print("========================")

    # 
    res = es.search(index=index, doc_type=doc, 
        body={"query": {"term": {"speaker": "WEST"}}})
    print("term")
    print(json.dumps(res))
    print("========================")

    #
    #res = es.search(index=index, doc_type=doc, 
    #body={"size":1, 
    #    "query": {"bool": {"must_not": {"match": {"speaker": "WEST"}}},
    #    {"should": {"match": {"speaker": "KING" }}}}})
    
    #print("must_not, should")
    #print(json.dumps(res))


    res = es.search(index=index, doc_type=doc, 
        body={"size": 2, "query": {"regexp": {"speaker": ""}}})
    
    print("reg_exp")
    print(json.dumps(res))
    print("========================")


if __name__  == "__main__":
    main()