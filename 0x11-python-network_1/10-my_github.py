#!/usr/bin/python3
"""
given username and pw as param, get your id from Github api
"""
from sys import argv
import requests
from requests.auth import HTTPBasicAuth


if __name__ == "__main__":
    url = 'https://api.github.com/user'
    creds = HTTPBasicAuth(argv[1], argv[2])
    req = requests.get(url, auth=creds)
    print(req.json().get('id'))
