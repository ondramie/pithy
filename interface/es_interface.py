#!/usr/bin/python3

""" Search interface for searching stack trace error in Stack Overflow
    elasticsearch repository that exits on four EC2 instances.  
"""

import json                                 # json.dumps()
import sys                                  # sys.argv()
from elasticsearch import Elasticsearch     # ES object
from Timer import MyTimer                   # class to record elapsed time
from my_ips import private_ips              # private ips for AWS instances
from pprint import pprint

def print_results(results, index, qtime):
    """ Exits for visually verifying search results"""
    print("START")
    print("Results %d in index %s took %.6g"%(results['hits']['total'], index, qtime))
    pprint(results['hits']['hits'][0]['_source'])
    print("END")

def search(es, ft_query, index, field, text, size):
    """ Searches ES in body of Stack Overflow posts for stack trace error
    """
    return es.search(index=index, 
                        size=size, 
                            doc_type=index, 
                                body={
                                    "query": {
                                            ft_query: {field: text}
                                    }
                    })

def answer(es, res, index):
    """ A post can be a question or answer. An accepted question has an 
        AcceptedAnswerId. A de-facto answer references its ParentId and has the 
        highest score. Checks if answer has an accepted id and if it does't than 
        returns higestest voted score""" 
    top_answer = None
    for answer in res['hits']['hits']:
        if answer['_source']['AcceptedAnswerId'] != None:
            AcceptedAnswerId = answer['_source']['AcceptedAnswerId'] 
        elif answer['_source']['ParentId'] != None:
            ParentId = answer['_source']["ParentId"]                       
            break

    if AcceptedAnswerId != None:
        top_answer = search(es, "term", index, "Id", AcceptedAnswerId, 1)['hits']['hits'][0]['_source']['Body']
    elif AcceptedAnswerId == None and ParentId != None:
        # Not an accepted answer but gets the top answer
        answers = search(es, "term", index, "ParentId", ParentId, 10)
        max_score = 0
        for answer in answers['hits']['hits']:
            if max_score < answer['_source']['_score']:
                max_score = answer['_source']['_score']
                top_answer = answer['_source']['Body']

    return top_answer 


def main(myError):     
    es = Elasticsearch(private_ips())                        # establishes client
    index = 'posts2'                                         # index to query ES 
    query_type = "match"                                     # type of query
    res = search(es, query_type, index, "Body", myError, 10)  
    if len(res) > 0:
        pprint(answer(es, res, index))


if __name__  == "__main__":
    try:
        main(sys.argv[1])
    except IOError:
            print(sys.stderr)
            sys.exit(1)