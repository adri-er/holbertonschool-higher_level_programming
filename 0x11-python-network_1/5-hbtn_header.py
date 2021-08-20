#!/usr/bin/python3
""" This module contains a script to fetch a URL """
import requests
import sys

if __name__ == "__main__":
    r = requests.get(sys.argv[1])
    print(r.headers.get('X-Request-Id'))
