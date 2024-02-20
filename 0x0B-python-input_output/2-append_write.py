#!/usr/bin/python3
"""
    Module 02 append_write
    funcs:
            append_write
"""


def append_write(filename="", text=""):
    """
    function that append text to the end of a file
    if file doesn't exist it creates it
    Returns:
        the number of chars added
    Args:
        filename: the file to manipulate
        text: the text to append
    """
    with open(filename, mode="a+", encoding="utf-8") as f:
        return (f.write(text))
