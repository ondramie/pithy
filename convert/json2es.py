#!/usr/bin/python3

'''Feeds json to Elasticsearch'''

import json                                         # build-in python package
import sys                                          # sys.argv()
import subprocess
from elasticsearch import Elasticsearch, helpers
from mappings_indices import Mappings, Indices
from pprint import pprint
from my_ips import private_ips


def load_es(file_name, bulk_size):
    json_name = str(file_name).split("/")[-1].split(".")[0].split("-")[-1].lower()
    maps = Mappings()
    indices = Indices()
    print("stackoverflow filename:\t", json_name)
    print("bulk_size:\t\t", bulk_size)

    es = Elasticsearch(private_ips(), request_timeout=5000)
    #subprocess.call("curl -XGET localhost:9200/_cluster/health?pretty=true", shell=True)
    #subprocess.call("curl -X GET localhost:9200/_cat/indices?v", shell=True)
    #subprocess.call("curl localhost:9200/_cat/nodes", shell=True)

    #es.indices.delete(index=json_name, ignore=[400, 404])
    es.indices.create(index=json_name, ignore=400, body=getattr(maps,json_name))  
    mem = getattr(indices, json_name)

    with open(file_name, "r") as inputs:
        actions = []
        for line in inputs:
            line_dic = json.loads(line)
            actions.append(mem(line_dic))
            if len(actions) == int(bulk_size):
                helpers.bulk(es, actions)
                actions = []

        if actions:
            helpers.bulk(es, actions)
            #es.index(index=json_name, doc_type=json_name, body=actions)

def main():
    load_es(sys.argv[1], sys.argv[2])

if __name__  == "__main__":
    main()
