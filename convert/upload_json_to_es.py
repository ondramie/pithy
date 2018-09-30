#!/usr/bin/python3

''' shebang /home/ubuntu/anaconda2/envs/p3/bin/python
    example.json input:

    {"index": {
        "_index": "Posts",
        "_id": "2"}}
    {"@Id": "2",
    "@PostTypeId": "1",
    "@AcceptedAnswerId": "28",
    "@CreationDate": "2012-03-06T19:06:05.667",
    "@Score": "18",
    "@ViewCount": "510",
    "@Body": "<p>The set difference operator ... </p>\n",
    "@OwnerUserId": "5",
    "@LastEditorUserId": "69",
    "@LastEditDate": "2012-04-02T15:35:05.827",
    "@LastActivityDate": "2013-05-29T00:50:34.590",
    "@Title": "Does the 'difference' operation add expressiveness to a query 
    language that already includes 'join'?",
    "@Tags": "<database-theory><relational-algebra><finite-model-theory>",
    "@AnswerCount": "2",
    "@CommentCount": "1",
    "@FavoriteCount": "1"}
'''

import json     	      # build-in package
import sys			      # sys.argv()
import os                 # os.listdir(); list of directory
import subprocess         # run shell scripts in python
import tqdm               # status of iterator
from elasticsearch import Elasticsearch, helpers   # helpers.bulk()

def load_json(directory):
    # searchs directory for .json files; loads json to generator 
    for filename in os.listdir(directory):
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
                    "@AcceptedAnswerId": {"type": "integer"},
                    "@CreationDate": {"type": "date"},
                    "@Score": {"type": "integer"},
                    "@ViewCount": {"type": "integer"},
                    "@Body": {"type": "text"},
                    "@OwnerUserId": {"type": "integer"},
                    "@LastEditorUserId": {"type": "integer"},
                    "@LastEditDate": {"type": "date"},
                    "@LastActivityDate": {"type": "date"},
                    "@Title": {"type": "text"},
                    "@Tags": {"type": "text"},
                    "@AnswerCount": {"type": "integer"},
                    "@CommentCount": {"type": "integer"},
                    "@FavoriteCount": {"type": "integer"}
                }
            }
        }
    }""")

    es.indices.create(index="posts", body=body)
    actions = []
    if sys.version_info[0] == 3 and len(sys.argv) == 2:
        try:
            for i, line in tqdm(enumerate(open(sys.argv[1]))):
                review = json.loads(line)
                actions.append({
                    "_index": "posts",
                    "_type": "review",
                    "_source": {
                    "@AcceptedAnswerId": review["@AcceptedAnswerId"],
                    "@CreationDate": review["@CreationDate"],
                    "@Score": review["@Score""],
                    "@ViewCount": review["@ViewCount"], #if "reviewerName" in review else None,
                    "@Body": review["@Body"],
                    "@OwnerUserId": review["@OwnerUserId"],
                    "@LastEditorUserId": review["@LastEditorUserId"],
                    "@LastEditDate": review["@LastEditDate"],
                    "@LastActivityDate": review["@LastActivityDate"],
                    "@Title": review["@Title"],
                    "@Tags": review["@Tags"],
                    "@AnswerCount": review["@AnswerCount"],
                    "@CommentCount": review["@CommentCount"],
                    "@FavoriteCount": review["@FavoriteCount"]
                    }
                })

            helpers.bulk(es, actions) 

            # queries
            res= es.search(index='megacorp',
                doc_type='employee',
                body={'query':{'match':{"about":"play cricket"}}}) 

            print(res)
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
