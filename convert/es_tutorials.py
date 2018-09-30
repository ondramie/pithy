#!/usr/bin/python3

'''Creates a subset of data to run on the elasticsearch'''

import sys              # sys.argv()
import json             # json.loads()

def main():
    with open(sys.argv[1], "r") as data, open("posts_small.json", "w") as output:
        count = 0
        #textfile = data.read()
        data = json.loads(data.read())
        print(type(data))
        #print(data[0])
        #for line in data: 
        #    if count < 20:
        #        output.write(json.dumps(line))
        #    else: 
        #        break
        #    count += 1

if __name__  == "__main__":
    main()
