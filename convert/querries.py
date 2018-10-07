#!/usr/bin/python3

''' Sample queries of error codes'''

import json     	                                # json.dumps()
import sys			                                # sys.argv()
from elasticsearch import Elasticsearch, helpers    # helpers.bulk()

def main():     
    es = Elasticsearch() 
    index="posts"

    # returns number of entries
    doc = {'size': 10000, 'query': { 'match_all': {}}}
    res = es.search(index='posts', doc_type='posts', body=doc)
    print("total number of documents %d in index %s"%(res['hits']['total'], index))

    # prints all the records 
    #res = es.search(index=index, doc_type=index, body=doc, scroll='1m')
    #scrollId = res['_scroll_id']
    #es.scroll(scroll_id = scrollId, scroll = '1m')

    # does the index exist? 
    res = es.indices.exists(index=index)
    print(res)

    # 
    res = es.search(index=index, doc_type=index, body={"query": 
    {"match_phrase": {"Body": "Math.Floor()"}}}) 
    #print(res['hits']['hits'])
    links = [entries['_source']['_source']['Id'] for entries in res['hits']['hits']]

    # websites
    sites = ["https://stackoverflow.com/questions/" + str(link) for link in links]
    print(sites)

if __name__  == "__main__":
    main()