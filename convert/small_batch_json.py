#!/usr/bin/python3

import sys              # sys.argv()
import json             # build-in python package

def main():
    with open(sys.argv[1], "r") as data, open("PostSmall.json", "w") as output:
        count = 0
        textfile = data.read()
        data = json.loads(textfile)
        #data = json.loads(data)
        #print(data[0])
        #for line in data: 
        #    if count < 20:
        #        output.write(json.dumps(line))
        #    else: 
        #        break
        #    count += 1

if __name__  == "__main__":
    main()
