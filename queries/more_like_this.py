#!/usr/bin/python3

'''This tests the match_phrase query from Elastic search'''

import json                                     # json.dumps()
import sys                                      # sys.argv()
from elasticsearch import Elasticsearch         # ES object library
from pprint import pprint
from RuntimeErrors import StackErrors           # errors used for benchmark 
from Timer import MyTimer                       # class to record elapsed time
from my_ips import private_ips                  # contains ips for AWS instances
from tqdm import tqdm                           # provides terminal output of progress


def match_phrase_answer(results, answers):
    ''' Checks the searched results against known answers to query for accuracy
        results = queried results
        answers = known answers for query'''
    correct = 0
    for result in results['hits']['hits']:
        Id = result['_source']['Id']
        if int(Id) in answers:
            correct = 1
            break 

    return correct

def more_like_this(es, index, trace, answer, request_timeout, size):
    '''The query filters for questions. A question would not have a ParentId; it is set to None
        es            = client
        index         = es index
        trace         = stack trace error
        answer        = reasonable list of acceptable answers for stack trace error (see RuntimeErrors.py)
        request_time  = time limit to recieve results back from elasticsearch
        size          = size of the number of results''' 
    output = []
    mytimer = MyTimer()
    results = es.search(index=index,size=size, doc_type=index, 
                        body={"query": {
                                            "more_like_this" : {
                                                "fields" : ["Body"],
                                                    "like" : trace,
                                                    "min_term_freq" : 1,
                                                    "max_query_terms" : 5
                                                }
                                            }
                            }, request_timeout=request_timeout)
    output.append((mytimer.get_end(), match_phrase_answer(results, answer))) 
    return output

def main():     
    es = Elasticsearch(private_ips())           # establishes client
    index = 'posts2'                            # index of ES 
    errors = StackErrors()                      # error under investigation
    rt = 180                                    # runtime 
    size = 165                                  # top 175 answers

    with open("accuracy_more_like_this.csv", "a") as output:
        # ran to get average of results
        for _ in tqdm(range(1000)):
            # iterate through known stacktrace errors and answers
            for stacktrace, error_answer in zip([errors._name, errors._index, errors._attrib], [errors.name(), errors.index(), errors.attrib()]):
                # iterate through the number slop
                [(time, correct)] = more_like_this(es, index, stacktrace, error_answer, rt, size)
                output.write("%s,\t%s\t%s\t%s,\n"%(stacktrace, "match", time, correct))

if __name__  == "__main__":
    main()