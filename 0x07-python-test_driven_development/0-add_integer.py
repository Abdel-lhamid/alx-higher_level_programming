#!/usr/bin/python3
"""
add-integer
Methode to return int sum of 2 ints
"""

def add_integer(a, b=98):
    """
    Returns sum of a and b as int
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    elif not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    else:
        return ( int(a) + int(b))

