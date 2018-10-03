#!/usr/bin/python3

import sys
from xml.dom.minidom import parseString

file = open(sys.argv[1],'r')
data = file.read()
file.close()

dom = parseString(data)
print(len(dom.getElementsByTagName('out')))



