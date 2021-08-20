#!/usr/bin/python3
""" This module contains a script to fetch a URL """
import requests
import sys


if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]
    post_add = {"email": email}
    r = requests.post(url, data=post_add)
    print(r.text)
