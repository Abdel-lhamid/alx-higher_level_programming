#!/usr/bin/python3
"""
    Model 01 Base Class
    contains the base CLass
"""
import json
import os


class Base():
    """
    Base Class for the project
    Attr:
            private attribute:  __nb_objects
            public instance attribute: id
    Funcs:
            to_json_string(list_dictionarie)
            save_to_file(cls, list_objs)
            from_json_string(json_string)
            create(cls, **dictionary)
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
            list_dictionaries = [obj.to_dictionary() for obj in list_objs]
        with open(cls.__name__ + ".json", "w", encoding="utf-8") as f:
            f.write(cls.to_json_string(list_dictionaries))

    @staticmethod
    def from_json_string(json_string):
        """
        returns the list of the JSON string representation json_string
        """
        if json_string is None:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """
        returns an instance with all attributes already set
        """
        if len(dictionary) > 1:
            rec = cls(1, 1)
        else:
            rec = cls(1)
        rec.update(**dictionary)
        return rec

    @classmethod
    def load_from_file(cls):
        """
        A method that returns a list of instances
        """
        file_path = cls.__name__ + ".json"
        if not os.path.exists(file_path) or os.stat(file_path).st_size == 0:
            return []
        with open(file_path, mode="r", encoding="utf-8") as f:
            dictionaries = cls.from_json_string(f.read())
        instances = []
        if dictionaries:
            for dic in dictionaries:
                instances.append(cls.create(**dic))
        return instances

