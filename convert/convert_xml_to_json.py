#!/home/ubuntu/anaconda2/envs/p3/bin/python
'''Converts xml file into json
   Usage: convert_xml_to_json.py <xml-file> >
'''

import json     			 # build-in python package
import sys				 # sys.argv()
import xmltodict

def convert(xml_file, xml_attribs=True):
    # TODO: read whole directory
    file_name = str(xml_file).split("/")[-1].split(".")[0]
    json_file  = file_name + ".json"
    out_path = "/home/ubuntu/Downloads/" + json_file
    #print("path", path)
    #print("xml_file", xml_file)
    with open(xml_file, "rb") as input, open(out_path, "w") as output:    # notice the "rb" mode
        d = xmltodict.parse(input, xml_attribs=xml_attribs)
        for i in d["posts"]["row"]:
            output.write(json.dumps({"index": {"_index": file_name, "_id": i["@Id"] }}, indent=4))
            output.write(json.dumps(i, indent=4))

def main():
    # sys.argv[1] = <json.file>
    if sys.version_info[0] == 3 and len(sys.argv) == 2:
        try:
            convert(sys.argv[1], True)
        except IOError:
            print(sys.stderr)
            sys.exit(1)

if __name__  == "__main__":
    main()
