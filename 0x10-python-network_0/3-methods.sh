#!/bin/bash
# Takes a URL and displays all HTTP methods the server will accept.
curl -s -X OPTIONS -I "$1" | grep "Allow: " | cut -b 8-
