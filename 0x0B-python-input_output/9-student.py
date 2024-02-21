#!/usr/bin/python3
"""
    Module 09 student
    contains Student Class, with attributes and methods
"""


class Student():
    """
    Class Student
    Attrs: first_name
           last_name
           age
    Methodes:
                to_json
    """
    def __init__(self, first_name, last_name, age):
        """
        Initializes student with first last name and age
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
    def to_json(self):
        """
        Returns dictionary description with simple data structure
        for Json serialization
        """
        return self.__dict__
