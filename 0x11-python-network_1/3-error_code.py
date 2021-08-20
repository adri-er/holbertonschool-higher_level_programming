#!/usr/bin/python3
""" Takes in a URL, sends a request to the URL and displays the body """
import urllib.request
import sys
import urllib.error


if __name__ == "__main__":
    req = Request(sys.argv[1])
    try:
        response = urlopen(req)
        print(str(response.read())[2:-1])
    except HTTPError as e:
        print("Error code:", e.code)
