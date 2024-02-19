#!/usr/bin/python3
"""
    Module 04 inherits_from
    funcs:
          inherits_from.

"""


def inherits_from(obj, a_class):
    """
    function that checks if obj is an instance
    of a class that only inherits from a_class

    Returns:
            True if so, otherwise False
    """
    return (issubclass(type(obj), a_class) and type(obj) is not a_class)
