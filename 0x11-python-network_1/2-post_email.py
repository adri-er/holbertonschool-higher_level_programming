#!/usr/bin/python3
""" Script to receive URL and email, sends a post request and display body. """
import urllib.request
import urllib.parse
import sys

url = sys.argv[0]
email = sys.argv[1]
value = {'email' : email}
data = urllib.parse.urlencode(value)
data = data.encode('ascii')
request = urllib.request.Request(url, data)
with urllib.request.urlopen(request) as response:
    answer = response.read()
    print(str(answer)[2:-1])
