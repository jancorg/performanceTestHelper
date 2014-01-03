#!/usr/bin/env python

import time
from urlparse import urlparse
import urllib2
from time import sleep
import threading
import sys
from mm_performance_test_helpers import RequestThread, PerformanceRequest

def performParallelRequests(base_url,requests_array,delay):
    # TODO

if __name__ == '__main__':
    base_url = "https//www.example.com"
    log = sys.argv[1]
    delay = sys.argv[2]

    f = open(log)
    lines= f.readlines()
    f.close()

    performParallelRequests(base_url,lines,delay)

