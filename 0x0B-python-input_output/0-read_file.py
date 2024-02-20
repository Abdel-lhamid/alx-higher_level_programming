#!/usr/bin/python3
"""
    Module 00 read-file
    funcs:
          read_file(filename="")
"""


def read_file(filename=""):
    """
    a function that reads and prints the content of a file
    args:
        filename: the file to read
    """
    with open(filename, mode="r", encoding="utf-8") as f:
        print(f.read())
