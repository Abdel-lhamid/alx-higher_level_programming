#!/usr/bin/python3
"""
    Model 01 Base Class
    contains the base CLass
"""
import json


class Base():
    """
    Base Class for the project
    Attr:
            private attribute:  __nb_objects
            public instance attribute: id
    Funcs:
            to_json_string(list_dictionarie)
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

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        returns the JSON string representation of list_dictionaries
        """

        if not list_dictionaries:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        writes the JSON string representation of list_objs to a file
        """

        list_dictionaries = []
        if list_objs:
            for obj in list_objs:
                list_dictionaries.append(obj.to_dictionary())
        with open(cls.__name__ + ".json", "w", encoding="utf-8") as f:
            f.write(cls.to_json_string(list_dictionaries))
