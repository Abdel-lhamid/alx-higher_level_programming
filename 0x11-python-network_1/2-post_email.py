#!/usr/bin/python3
"""
given URL, email as params, send POST req to URL, display response body utf-8
"""
from sys import argv
from urllib import parse,request


if __name__ == "__main__":
    url = argv[1]
    email = {'email': argv[2]}
    data = parse.urlencode(email).encode('ascii')
    req = request.Request(url, data)
    with request.urlopen(req) as response:
        print(response.read().decode("utf-8"))
