#!/usr/bin/python3

'''Extracts data from S3, converts xml to json by pyspark job   
   NOTE: alternative shebang: 
        !/home/ubuntu/anaconda2/envs/p3/bin/python
   NOTE: ~/ == ./home/unbuntu'''

import json                                         # build-in python package
import sys                                          # sys.argv()
import xmltodict                                    # .parse()
import subprocess
import boto
import xml.etree.ElementTree as etree
from elasticsearch import Elasticsearch, helpers
from mappings_indices import Mappings, Indices
#from pprint import pprint

def load_es(xml_file, xml_attribs=True):
    # TODO:   read whole directory 
    #file_name = str(xml_file).split("/")[-1].split(".")[0].split("-")[-1].lower() #small batch
    file_name = str(xml_file).split("/")[-1].split(".")[-1].split("-")[-1].lower()
    print(file_name)
    json_file  = file_name + ".json"  
    out_path = "/home/ubuntu/Downloads/" + json_file
    
    with open(xml_file, "rb") as inputs, open(out_path, "w") as out:
        # TODO: xmltodict reads into memory; need spark job or iterate through the data     
        mem = getattr(indices, file_name)
        for event, elem in etree.iterparse(inputs, events=('start', 'end', 'start-ns', 'end-ns')):
            if event == "start" and elem.tag == 'row':
                es.index(index=file_name, doc_type=file_name, body=mem(elem.attrib))
            if event == "end": 
                elem.clear() 

def main():
    # sys.argv[1] = <xxx.xml>
    if sys.version_info[0] == 3 and len(sys.argv) == 2:
        try:
            load_es(sys.argv[1], True)
        except IOError:
            print(sys.stderr)
            sys.exit(1)

if __name__  == "__main__":
    main()