#!/usr/bin/python3
"""
given URL & email as params, send POST req to URL, display response body utf-8
"""
from sys import argv
import requests

if __name__ == "__main__":
    url = argv[1]
    payload = {'email': argv[2]}
    req = requests.post(url, data=payload)
    print(req.text)
