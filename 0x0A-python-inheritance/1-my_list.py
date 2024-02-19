#!/usr/bin/python3
"""
class MyList that inherits from list,
with Public instance method: def print_sorted(self):
that prints the list, but sorted (ascending sort)
"""


class MyList(list):
    """
    class that inherists from List,
    methode print_sorted
    """
    def print_sorted(self):
        """
        prints the list, but sorted (ascending sort)
        """
        print(sorted(self))
