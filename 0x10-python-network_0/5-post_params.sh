#!/bin/bash
# takes a URL, sends a POST and displays body
curl -s -I -X POST -d "email=hr@holbertonschool.com&subject=I will always be here for PLD" "$1"
