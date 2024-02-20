#!/usr/bin/python3
"""
    Module 01 write-file
    funcs:
            write_file(filename="", text="")
"""


def write_file(filename="", text=""):
    """
    function that writes to a file the text given
    if the file exists it over wright it
    if not it creates the file

    Args:
          filename: the file to overwrite or create
          text: the text to write on the file
    Returns:
            the number of chars writen in the file
    """
    with open(filename, mode="w", encoding="utf-8") as f:
       return (f.write(text))
