#!/usr/bin/python3
"""
    Module 06 load_from_json_file
    funcs:
        def load_from_json_file(filename)
"""


def load_from_json_file(filename):
    """
    a function that creates an Object from a “JSON file”
    Returns:
        a python object from the json file
    Args:
        filename: tha file to get the obj from
    """
    import json
    with open(filename, mode="r", encoding="utf-8") as f:
        return json.load(f)
