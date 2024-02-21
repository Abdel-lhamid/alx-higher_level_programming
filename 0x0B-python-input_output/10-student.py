#!/usr/bin/python3
"""
    Module 10 student
    contains Student Class, with attributes and methods
"""


class Student():
    """
    Class Student
    Attrs: first_name
           last_name
           age
    Methodes:
                to_json(self, attrs=None)
    """
    def __init__(self, first_name, last_name, age):
        """
        Initializes student with first last name and age
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Returns dictionary description with simple data structure
        for Json serialization, if attrs passed only return those
        """
        if attrs is None:
            return self.__dict__
        else:
            dics = {}
            for a in attrs:
                if a in self.__dict__.keys():
                    dics[a] = self.__dict__[a]
            return dics
