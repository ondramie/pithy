#!/home/ubuntu/anaconda2/envs/p3/bin/python
'''Uploads json into elasticsearch'''

import json     			           # build-in python package
import sys					   # sys.argv()
from elasticsearch import Elasticsearch, helpers   # bulk
import os					   # os.listdir(); list of directory
import subprocess				   # shell scripts

def load_json(directory):
    '''Use a generator, no need to load all in memory'''
    for filename in os.listdir(directory):
        print("filename:\t", filename)
        if filename.endswith('.json'):
            input  = directory + filename
            with open(input,'r') as open_file:
                yield(json.load(open_file))

def main():
    es = Elasticsearch()
    body = json.loads("""{
        "mappings": {
             "posts": {
                  "properties": {
                     "@id":         {"type": "keyword"},
                     "@PostTypeId": {"type": "keyword"},
                     "@AcceptedAnswerId": {"type": "text"},
                     "@CreationDate": {"type": "date"},
                     "@Score": {"type": "float"},
                     "@ViewCount": {"type": "float"},
                     "@Body": { "type": "text"},
                     "@OwnerUserId": {"type": "float"},
                     "@LastEditorUserId": {"type": "float"},
                     "@LastEditDate": {"type": "date"},
                     "@LastActivityDate": {"type": "date"},
                     "@Title": { "type": "text" },
                     "@Tags": { "type": "float"},
                     "@AnswerCount": {"type": "float"},
                     "@CommentCount": {"type": "float"},
                     "@FavoriteCount": {"type": "float"}
                      }
                    }
              }
          }
        }""")

    es.indices.create(index="posts", body=body)
    
    if sys.version_info[0] == 3 and len(sys.argv) == 2:
        try:
            # print("input file", sys.argv[1])
            #print(*
            load_json(sys.argv[1]) #)
            #helpers.bulk(es, load_json(sys.argv[1]), index='my-index', doc_type='my-type')
            # "@Id": "1810902"

            # print(es.search(index="my-index", q='@PostId:"393"'))                # queries es
            #print(es.get(index='my-index', doc_type='my-type',"@id"="1910902"))
            #subprocess.call("curl 'localhost:9200/_cat/indices?v'", shell=True)  # bash checks es
        except IOError:
            print(sys.stderr)
            sys.exit(1)


if __name__  == "__main__":
    main()
