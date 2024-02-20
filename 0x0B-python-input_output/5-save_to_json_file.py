#!/usr/bin/python3
"""
    Module 05 save_to_json_file
    funcs:
        save_to_json_file(my_obj, filename)
"""


def save_to_json_file(my_obj, filename):
    """
    a function that writes an Object to a text file,
    using a JSON representation
    Args:
        my_obj: the object to store as json format and save to the file
        filename: the file to save the object to
    """
    import json
    with open(filename, mode="w+", encoding="utf-8") as f:
        json.dump(my_obj, f)
