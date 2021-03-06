#!/usr/bin/python3

'''Converts xml file into json file
   Usage: convert_xml_to_es.py <xml-file>
   NOTE: alternative shebang: 
        !/home/ubuntu/anaconda2/envs/p3/bin/python
   NOTE: ~/ == ./home/unbuntu'''

import json                                         # build-in python package
import sys                                          # sys.argv()
import xmltodict                                    # .parse()
import subprocess
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

    maps = Mappings()
    indices = Indices()

    es = Elasticsearch()
    es.indices.delete(index=file_name, ignore=[400, 404])     # deletes if exists
    #subprocess.call("curl -XGET localhost:9200/_cluster/health?pretty=true", shell=True)
    #subprocess.call("curl -X GET localhost:9200/_cat/indices?v", shell=True)
    #es.indices.create(index=file_name, ignore=400, body=getattr(maps, file_name))
    
    with open(xml_file, "rb") as inputs, open(out_path, "w") as out:
        # TODO: xmltodict reads into memory; need spark job or iterate through the data     
        mem = getattr(indices, file_name)
        for event, elem in etree.iterparse(inputs, events=('start', 'end', 'start-ns', 'end-ns')):
            #es.indices.create(index=file_name, ignore=400, body=getattr(maps, file_name))
            if event == "start" and elem.tag == 'row':
                #print(mem(elem.attrib))
                #helpers.bulk(es, mem(elem.attrib))
                es.index(index=file_name, doc_type=file_name, body=mem(elem.attrib))
            if event == "end": 
                elem.clear() 

        #dic = xmltodict.parse(inputs, xml_attribs=xml_attribs)  # converts xml to json
        #out.write(json.dumps(dic, indent=2))
        #for index, i in enumerate(dic[file_name]["row"]):
            #pprint([mem(i) for i in dic[file_name]["row"]])
        #helpers.bulk(es, (mem(i) for i in dic[file_name]["row"]))

    subprocess.call("curl -X GET localhost:9200/_cat/indices?v", shell=True)

def main():
    # sys.argv[1] = <xxx.json>
    if sys.version_info[0] == 3 and len(sys.argv) == 2:
        try:
            load_es(sys.argv[1], True)
        except IOError:
            print(sys.stderr)
            sys.exit(1)

if __name__  == "__main__":
    main()