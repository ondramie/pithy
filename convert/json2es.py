#!/usr/bin/python3

'''Extracts data from S3, converts xml to json by pyspark job   
   NOTE: alternative shebang: 
        !/home/ubuntu/anaconda2/envs/p3/bin/python
   NOTE: ~/ == ./home/unbuntu
   '''

import json                                         # build-in python package
import sys                                          # sys.argv()
import subprocess
from elasticsearch import Elasticsearch, helpers
from mappings_indices import Mappings, Indices
from pprint import pprint

def load_es(file_name):
    json_name = str(file_name).split("/")[-1].split(".")[0].split("-")[-1].lower()
    maps = Mappings()
    indices = Indices()
    print("stackoverflow filename:\t", json_name)

    # NOTE: elastics nodes with 6.4.2:
    es = Elasticsearch()
    
    #es = Elasticsearch()
    #subprocess.call("curl -XGET localhost:9200/_cluster/health?pretty=true", shell=True)
    #subprocess.call("curl -X GET localhost:9200/_cat/indices?v", shell=True)
    #subprocess.call("curl localhost:9200/_cat/nodes", shell=True)

    es.indices.delete(index=json_name, ignore=[400, 404])
    es.indices.create(index=json_name, ignore=400, body=getattr(maps,json_name))  
    mem = getattr(indices, json_name)

    with open(file_name, "r") as inputs:
        actions = []
        for line in inputs:    
            line_dic = json.loads(line)
            actions.append(mem(line_dic))
            if len(actions) == 1000: 
                #print(mem(line_dic))
                #print(count)
                #print(actions)
                #es.index(index=json_name, doc_type=json_name, body=actions)
                helpers.bulk(es, actions)
                del actions[:]

        if actions:
            helpers.bulk(es, actions)
            #es.index(index=json_name, doc_type=json_name, body=actions)
            #         
    #subprocess.call("curl -X GET localhost:9200/_cat/indices?v", shell=True)

def main():
    # sys.argv[1] = <xxx.xml>
    load_es(sys.argv[1])

if __name__  == "__main__":
    main()