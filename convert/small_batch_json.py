#!/usr/bin/python3

'''Creates a subset of data to run on the elasticsearch'''

import sys              # sys.argv()
import json             # json.loads()

def main():
    with open(sys.argv[1], "r") as data, open("posts_small.json", "w") as output:
        centimator = 100
        for index, line in enumerate(data):
            if index % centimator == 3: 
                #print(line)
                f = json.loads(line)
                if len(f) > 1: 
                    output.write(json.dumps(f, indent=2))
                
if __name__  == "__main__":
    main()
