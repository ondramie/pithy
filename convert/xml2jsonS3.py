#!/usr/bin/python3

''' Connects to s3 storage; converts an XML file into JSON file. 
    Performs the task two differnt wasy. Both are done sequentially and the 
    convesion is saved to remote instance. Processing sequentially and locally 
    took a long time (+10hrs). Final solution did not employ this method. 
    Please see spark folder
'''

import json                                 # string 2 dictionary
from smart_open import smart_open           # opens S3 file sequentially
import xml.etree.ElementTree as etree       # parses XML
from xml.etree import ElementTree           
from tqdm import tqdm                       # status of iteration in terminal
import sys                                  # sys.argv()

""" S3 bucket contains stackexchange an stackoverflow data. Several different 
    sizes of data were ingested into elastic search to determine speed of 
    ingestion.  
    
    FOLDER_NAME = "cs.stackexchange.com"   
    FILE_NAME   = "stackoverflow.com-PostLinks" 
                  "Badges.xml" 
"""

BUCKET_NAME =  "stack-overflow-s3-bucker" 
FILE_NAME   =  "stackoverflow.com-Posts"      

def stream_s3_object(bucket, files):
    """ Process file by opening xml file from S3 bucket and saves on remote 
        EC2 instance""" 
    input_file  = "s3://" + bucket + "/" + files 
    output_file = "s3://" + bucket + "/" + files  + ".json"
    with smart_open(input_file, 'rb') as ins, smart_open(output_file, 'w') as outs:
        for event, elem in etree.iterparse(ins, events=('start', 'end', 'start-ns', 'end-ns')):
            if event == "start" and elem.tag == 'row':
                outs.write(json.dumps(elem.attrib)) 
            if event == "end": 
                elem.clear()     


def stream_local(in_file):
    """ Processes xml file saved on remote EC2 instance
        NOTE: two files types exist on S3. Parse was done either by: 
        out_file = str(in_file).split('/')[-1].split('.')[0].lower() + ".json"
        out_file = str(in_file).split("/")[-1].split(".")[-1].split("-")[-1].lower() + ".json"
    """
    out_file = str(in_file).split("/")[-1].split(".")[-1].split("-")[-1].lower() + ".json"
    with open(out_file, "w") as outs:
        contents = etree.iterparse(in_file, events=('start', 'end'))
        contents = iter(contents)
        event, root = next(contents)
        for event, elem in tqdm(contents):
            if event == 'end' and elem.tag == "row": 
                outs.write(json.dumps(elem.attrib) + "\n")    # NOTE:hack
            root.clear()   


def main():
    if len(sys.argv) < 2: 
        stream_s3_object(BUCKET_NAME, FILE_NAME)
    else:
        stream_local(sys.argv[1])


if __name__  == "__main__":
    main()