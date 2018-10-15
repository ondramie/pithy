#!/usr/bin/python3

''' This class is used to capture start and end times of function calls.'''

import time

class MyTimer:
    def __init__(self): 
        self._start = time.time()
        self.end    = 0
    
    def get_end(self): 
        self.end = time.time() - self._start
        return self.end