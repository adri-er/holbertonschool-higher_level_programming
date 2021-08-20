#!/usr/bin/python3
""" This module contains a script to fetch a URL """
import urllib.request
with urllib.request.urlopen('https://intranet.hbtn.io/status') as request:
    print ("Body response:")
