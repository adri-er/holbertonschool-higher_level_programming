#!/usr/bin/python3
""" This module contains a script to display body and check if Error """
import requests
import sys


if __name__ == "__main__":
    r = requests.get(sys.argv[1])
    if r.status_code == requests.codes.ok:
        print(r.text)
    else:
        print("Error code:", r.status_code)
