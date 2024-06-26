#!/usr/bin/python3
"""
given URL & email as params, display response body utf-8, print error codes
"""
from sys import argv
from urllib import request, error


if __name__ == "__main__":
    try:
        with request.urlopen(argv[1]) as response:
            print(response.read().decode('utf-8'))
    except error.HTTPError as e:
        print("Error code: {}".format(e.code))
