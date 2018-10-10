#!/usr/bin/python3

'''This code connects to s3 storage and converts an XML file into JSON file
   
   NOTE: alternative shebang: 
        !/home/ubuntu/anaconda2/envs/p3/bin/python
   NOTE: ~/ == ./home/unbuntu
'''

import json                                 # string 2 dictionary
from smart_open import smart_open           # opens S3 file sequentially
import xml.etree.ElementTree as etree       # parses XML
from xml.etree import ElementTree
from tqdm import tqdm
import sys                                  #sys.argv()

BUCKET_NAME =  "stack-overflow-s3-bucker"   #FOLDER_NAME =  "cs.stackexchange.com"  
FILE_NAME   =  "stackoverflow.com-Posts"    #"stackoverflow.com-PostLinks" #"Badges.xml" #"stackoverflow.com-PostLinks"  

def stream_s3_object(bucket, files): #, file): 
    input_file  = "s3://" + bucket + "/" + files 
    # + folder + "/" + file
    output_file = "s3://" + bucket + "/" + files  + ".json"
    # + folder + "/" + file + ".json"
    with smart_open(input_file, 'rb') as ins, smart_open(output_file, 'w') as outs:
        for event, elem in etree.iterparse(ins, events=('start', 'end', 'start-ns', 'end-ns')):
            if event == "start" and elem.tag == 'row':
                outs.write(json.dumps(elem.attrib)) 
            if event == "end": 
                elem.clear()     

def stream_local(in_file):
    #out_file = str(in_file).split('/')[-1].split('.')[0].lower() + ".json"
    out_file = str(in_file).split("/")[-1].split(".")[-1].split("-")[-1].lower() + ".json"
    #print(in_file)
    with open(out_file, "w") as outs:
        contents = etree.iterparse(in_file, events=('start', 'end'))
        contents = iter(contents)
        event, root = next(contents)
        for event, elem in tqdm(contents):
            if event == 'end' and elem.tag == "row": 
                #print(type(elem.attrib))
                outs.write(json.dumps(elem.attrib) + "\n")    # hack
                #json.dump(elem.attrib, outs)
            root.clear()   
        
        #for event, elem in tqdm(etree.iterparse(in_file, events=('start', 'end'))):
        #    if event == "start" and elem.tag == 'row': 
        #        print(elem)
        #        #outs.write(str(elem.attrib) + "\n")
        #    elem.clear()

    #with open(in_file, "rb") as ins,  open(out_file, "w") as outs: 
    #    for event, elem in tqdm(etree.iterparse(ins, events=('start', 'end', 'start-ns', 'end-ns'))):
    #        if event == "start" and elem.tag == 'row':
    #            outs.write(json.dumps(elem.attrib))
    #        if event == "end": 
    #            elem.clear() 


def main():
    #if len(sys.argv) < 2: 
        # stream_s3_object(BUCKET_NAME, FILE_NAME)
        # #FOLDER_NAME, FILE_NAME)
    #else:
    stream_local(sys.argv[1])

if __name__  == "__main__":
    main()