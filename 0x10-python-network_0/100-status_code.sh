#!/bin/bash
# Passes hte status code without pipes
curl -s -o /dev/null -w "%{http_code}" "$1"
