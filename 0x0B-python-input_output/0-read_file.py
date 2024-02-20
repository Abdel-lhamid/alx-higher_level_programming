#!/usr/bin/python3
"""
    Module 00 read-file
    funcs:
          read_file(filename="")
"""


def read_file(filename=""):
    with open(filename, encoding="utf-8") as f:
        read_data = f.read()
        print(read_data)
        f.closed
