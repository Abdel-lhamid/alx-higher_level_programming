#!/usr/bin/python3
"""
    Module 10  and now the Square
    class: Square
    funcs:
        __init__
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """
        Class Square inherits Rectangle square
        funcs:
                def __init__(self, size, x=0, y=0, id=None)

    """
    def __init__(self, size, x=0, y=0, id=None):
        """
            initialization
        """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        return "[Square] ({:d}) {:d}/{:d} - {:d}\
                ".format(self.id, self.x, self.y, self.width)

    @property
    def size(self):
        """
            getter for size
        """
        return self.width

    @size.setter
    def size(self, value):
        """
            setter
        """
        self.width = value
        self.heigh = value

    def update(self, *args, **kwargs):
        """
            methode that update attributes
        """
        funcs = ["id", "size", "x", "y"]
        if args:
            for i in range(len(args)):
                setattr(self, funcs[i], args[i])
        else:
            for k, v in kwargs.items():
                setattr(self, k, v)

    def to_dictionary(self):
        """
        A function that returns the dictionary presentation of an obj
        """
        dic = {}
        list_attrs = ["id", 'x', "size", 'y']
        list_vals = [self.id, self.x, self.size, self.y]

        for k, v in zip(list_attrs, list_vals):
            dic[k] = v

        return dic
