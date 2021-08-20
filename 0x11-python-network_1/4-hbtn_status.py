#!/usr/bin/python3
""" This module contains a script to fetch a URL """
import requests


if __name__ == "__main__":
    r = requests.get('https://intranet.hbtn.io/status')
    print("Body response:")
    txt = r.text
    print("\t- type:", type(txt))
    print("\t- content:", txt)
