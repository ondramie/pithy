#!/usr/bin/python3

'''Extracts data from S3, converts xml to json by pyspark job   
   NOTE: alternative shebang: 
        !/home/ubuntu/anaconda2/envs/p3/bin/python
   NOTE: ~/ == ./home/unbuntu
   NOTE: ubuntu@ip-172-31-86-160 
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

    # NOTE: elastics nodes with 6.4.2:  'http://54.152.44.95:9200', 
    es = Elasticsearch(['54.209.55.117:9200',
                        '18.205.23.187:9200',
                        '54.88.62.138:9200',
                        '54.210.232.252:9200'])
    
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