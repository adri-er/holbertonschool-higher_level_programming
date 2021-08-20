#!/usr/bin/python3
""" Scrip that takes URL, sends request and disp value X-Request-Id """
import urllib.request
import sys


if __name__ == "__main__":
    with urllib.request.urlopen(sys.argv[1]) as request:
        print(request.info().get('X-Request-Id'))
