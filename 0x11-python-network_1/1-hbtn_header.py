#!/usr/bin/python3
""" Scrip that takes URL, sends request and disp value X-Request-Id """
import urllib.request
import sys


with urllib.request.urlopen(sys.argv[1]) as request:
    print(request.info()['X-Request-Id'])
