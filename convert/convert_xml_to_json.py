#!/home/ubuntu/anaconda2/envs/p3/bin/python
'''Converts xml file into json
   Usage: convert_xml_to_json.py <xml-file> >
'''

import json     			           # build-in python package
import sys					   # sys.argv()
import xmltodict

def convert(xml_file, xml_attribs=True):
    # TODO: print to folder of downloads; read whole directory
    json_file  = str(xml_file).split("/")[-1].split(".")[0] + ".json"
    path = "~/Downloads/" + json_file
    with open(xml_file, "rb") as f, open(path, "w") as out:    # notice the "rb" mode
        d = xmltodict.parse(f, xml_attribs=xml_attribs)
        out.write(json.dumps(d, indent=4))

def main():
    if sys.version_info[0] == 3 and len(sys.argv) == 2:
        try:
            convert(sys.argv[1], True)
        except IOError:
            print(sys.stderr)
            sys.exit(1)

if __name__  == "__main__":
    main()
