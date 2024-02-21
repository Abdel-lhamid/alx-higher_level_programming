#!/usr/bin/python3
"""
    Module 08 Class to json
    Funcs:
            class_to_json(obj)
"""


def class_to_json(obj):
    """
    class_to_json - a function that returns the dictionary
    description with simple data structure
    Args:
        obj: an object
    Returns:the dictionary description with simple data structure
            JSON serialization
    """
    return obj.__dict__
