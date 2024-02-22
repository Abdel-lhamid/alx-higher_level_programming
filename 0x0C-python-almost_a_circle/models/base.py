#!/usr/bin/python3
"""
    Model 01 Base Class
    contains the base CLass
"""


class Base():
    """
    Base Class for the project
    Attr:
            private attribute:  __nb_objects
            public instance attribute: id
    """
    __nb_object = 0
    def __init__(self, id=None):
        """
        the class constructor
        we assign id if passed if not we incriment
        the nb_object and assign it to id
        args:
            id: the id of the instance
        """
        if id is None:
            Base.__nb_object += 1
            self.id = Base.__nb_object
        else:
            self.id = id
