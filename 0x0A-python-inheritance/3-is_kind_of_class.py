#!/usr/bin/python3
"""
    Module 03 is_kind_of_class
    funcs:
    is_kind_of_class
"""


def is_kind_of_class(obj, a_class):
    """
    A function check if the obj is instance of a calss
    or a child class of a_class.
    Returns:
       True if obj is instan...., and False otherwise
    """
    return isinstance(obj, a_class)
