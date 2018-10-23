#!/usr/bin/python3

''' This tests the match_phrase query from Elastic search. A match_phrase 
    query analyzes the text and creates a "phrase." Use match_phrase to match 
    exact sequences of words or phrases. A phrase query matches terms up to a 
    configurable slop (which defaults to 0) in any order. Transposed terms have 
    a slop of 2.
'''

import json                                                 # json.dumps()
import sys                                                  # sys.argv()
from elasticsearch import Elasticsearch                     # ES object library
from pprint import pprint
from RuntimeErrors import StackErrors                       # errors used for benchmark 
from Timer import MyTimer                                   # class to record elapsed time
from my_ips import private_ips                              # contains ips for AWS instances
from tqdm import tqdm                                       # shows program progress in terminal


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


def match_phrase(es, index, trace, answer, request_timeout, slop, size):
    '''The query filters for questions. A question would not have a ParentId; 
       it is set to None
        es            = client
        index         = es index
        trace         = stack trace error
        answer        = reasonable list of acceptable answers for stack trace 
                        error (see RuntimeErrors.py)
        request_time  = time limit to recieve results back from elasticsearch
        slop          = mixture of word swaps 
        size          = size of the number of results''' 
    output = []
    for analyzer in ["simple", "standard", "stop"]:
        '''Iterates over analyzers for match_phrase query
           standard = The standard analyzer divides text into terms on word 
                      boundaries, as defined by the Unicode Text Segmentation 
                      algorithm. It removes most punctuation, lowercases terms, 
                      and supports removing stop words
           simple   = The simple analyzer divides text into terms whenever it 
                      encounters a character which is not a letter. It lowercases 
                      all terms    
           stop     = The stop analyzer is like the simple analyzer, but also 
                      supports removal of stop words.'''
        mytimer = MyTimer()
        results = es.search(index=index,size=size, doc_type=index, 
                            body={
                                "query": {
                                    "bool": {
                                        "should": [{
                                            "bool": {"must_not": {"exists": {"field": "ParentId"}}}},
                                        {
                                            "match_phrase": {"Body": { 
                                                                "query" : trace,
                                                                "analyzer": analyzer,
                                                                "slop": slop
                                                                }
                                                            }
                                            }]
                                    }
                                }
                            }, request_timeout=request_timeout)

        output.append((analyzer, mytimer.get_end(), match_phrase_answer(results, answer))) 
    return output


def main():     
    es = Elasticsearch(private_ips())           # establishes client
    index = 'posts2'                            # index of ES 
    errors = StackErrors()                      # error under investigation
    rt = 180                                    # runtime 
    size = 50                                   # top 50 answers

    with open("accuracy_filter.csv", "a") as output:
        # ran to get average of results
        for _ in tqdm(range(1000)):
            # iterate through known stacktrace errors and answers
            for stacktrace, error_answer in zip([errors._name, errors._index, errors._attrib], [errors.name(), errors.index(), errors.attrib()]):
                # iterate through the number slop
                for slop in range(len(stacktrace.split())): 
                    for analyzer, time, correct in match_phrase(es, index, stacktrace, error_answer, rt, slop, size):
                        output.write("%s,\t%s\t%s\t%s\t%s,\n"%(stacktrace, analyzer, time, slop, correct))

if __name__  == "__main__":
    main()
