#!/usr/bin/python3
import json
"""
    Module 03 to_json_string
    funcs:
        to_json_string(my_obj)
"""


def to_json_string(my_obj):
    """
    A function the returns the json representation of an obj
    Return:
        Obj in Json format
    Args:
        my_obj: an object
    """
    return (json.dumps(my_obj))
