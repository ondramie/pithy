#!/usr/bin/python3

''' This code uploads the following formated json to elastic search:  
    {"index": {"_index":"shakespeare","_id": 0}}
    {"type":"act",
     "line_id": 1,
     "play_name":"Henry IV", 
     "speech_number":"",
     "line_number":"",
     "speaker":"",
     "text_entry":"ACT I"}
'''

import json     	      # build-in package
import sys			      # sys.argv()
import subprocess         # run shell scripts in python
from elasticsearch import Elasticsearch, helpers   # helpers.bulk()

def upload(json_file):
    actions = []
    with open(json_file, "r") as json_in: 
        for line in json_in:
            d = json.loads(line) 
            if len(d) > 1: 
                actions.append({"_index": "shakespeare",
                    "_type": "doc",
                    "_source": {
                        "speaker": d["speaker"],
                        "play_name": d["play_name"],
                        "line_id": d["line_id"],
                        "speech_number": d["speech_number"]
                        } 
                    })
    return actions

def main():     
    es = Elasticsearch()
    body = json.loads('''{
        "mappings": {
            "doc": {
                "properties": {
                    "speaker": {"type": "keyword"},
                    "play_name": {"type": "keyword"},
                    "line_id": {"type": "integer"},
                    "speech_number": {"type": "integer"}
                    }
                }
            }
        }''')
    
    es.indices.create(index="shakespeare", ignore=400, body=body)
    helpers.bulk(es, upload(sys.argv[1]))

    # verifies creation of indices
    subprocess.call("curl -X GET localhost:9200/_cat/indices?v", shell=True)
    
    # simple queries
    res = es.search(index="shakespeare", doc_type="doc", 
        body={"query": {"match": {"speaker": "WEST*"}}})

    print(json.dumps(res, indent=2))

if __name__  == "__main__":
    main()
