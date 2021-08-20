#!/usr/bin/python3
""" Takes in a URL, sends a request to the URL and displays the body """
import urllib.request
import sys
import urllib.error


if __name__ == "__main__":
    try:
        with urllib.request.urlopen(sys.argv[1]) as response:
            print(str(response.read())[2:-1])
    except urllib.error.HTTPError as e:
        print("Error code:", e.code)
