#!/usr/bin/python3
import json
"""
    Module 04 from_json_string
    funcs:
        from_json_string(my_str)
"""


def from_json_string(my_str):
    """
    a function that return a py object from a json
    Return: a python object
    Args:
        my_str: the json format object to convert
    """
    return (json.loads(my_str))
