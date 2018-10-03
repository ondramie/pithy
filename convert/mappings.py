#!/usr/bin/python3

'''Converts xml file into json file
   Usage: convert_xml_to_es.py <xml-file>
   NOTE: alternative shebang: 
        !/home/ubuntu/anaconda2/envs/p3/bin/python
   NOTE: ~/ == ./home/unbuntu'''

import json             # build-in python package
import sys              # sys.argv()
import xmltodict        # .parse()
 

def convert_xml(xml_file, xml_attribs=True):
    # TODO:   read whole directory 
    # INPUT:  xml_file = /XXXX/XXX.xml
    # OUTPUT: XXX.json
    file_name = str(xml_file).split("/")[-1].split(".")[0]
    json_file  = file_name + ".json"
    out_path = "/home/ubuntu/Downloads/" + json_file

    with open(xml_file, "rb") as inputs, open(out_path, "w") as output:
        d = xmltodict.parse(inputs, xml_attribs=xml_attribs)
        for i in d["posts"]["row"]:
            # creates index for elasticSearch format 
            output.write(json.dumps({"index": 
                {"_index": file_name, "_id": i["@Id"]}})+ "\n") #, indent=4))
            output.write(json.dumps(i) + "\n") #, indent=4))

def main():
    # sys.argv[1] = <xxx.json>
    if sys.version_info[0] == 3 and len(sys.argv) == 2:
        try:
            convert(sys.argv[1], True)
        except IOError:
            print(sys.stderr)
            sys.exit(1)

if __name__  == "__main__":
    main()