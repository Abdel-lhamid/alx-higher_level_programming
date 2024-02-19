#!/usr/bin/python3
"""
Module 02-is_same_class

funcs:
    is_same_class(obj, a_class)
"""


def is_same_class(obj, a_class):
    """
    functtion that checks if an obj is an instance of a specified class

    Returns:
       True if obj is an intance of a specified class, otherwise False
    """
    return type(obj) == a_class
