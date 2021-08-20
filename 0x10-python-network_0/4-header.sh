#!/bin/bash
# takes an URL, sends a request and displays body
curl -s -I "$1" -H "X-HolbertonSchool-User-Id: 98"
