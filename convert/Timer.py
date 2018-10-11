#!/usr/bin/python3

''' This class is used to capture start and end times of function calls.'''

import time

class MyTimer:
    def __init__(self): 
        self.start = time.time()
    def end(self): 
        return time.time() - self.start