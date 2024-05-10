#!/usr/bin/python3
"""
given letter as param, POST to http://0.0.0.0:5000/search_user
"""
from sys import argv
import requests


if __name__ == "__main__":
    if len(argv) < 2:
        letter = ""
    else:
        letter = argv[1]
    url = 'http://0.0.0.0:5000/search_user'
    payload = {'q': letter}
    req = requests.post(url, data=payload)

    try:
        res = req.json()
        if res:
            print("[{}] {}".format(res.get('id'), res.get('name')))
        else:
            print("No result")
    except ValueError as e:
        print("Not a valid JSON")
