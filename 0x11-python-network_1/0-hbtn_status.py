#!/usr/bin/python3
""" This module contains a script to fetch a URL """
import urllib.request


if __name__ == "__main__":
    with urllib.request.urlopen('https://intranet.hbtn.io/status') as request:
        information = request.read()
        print("Body response:")
        print("\t- type:", type(information))
        print("\t- content:", information)
        print("\t- utf8 content:", str(information)[2:-1])
