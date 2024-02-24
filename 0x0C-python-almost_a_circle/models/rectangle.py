#!/usr/bin/python3
"""
    Module 02 Rectangle class
"""


from models.base import Base


class Rectangle(Base):
    """
    class Rectangle that inherites from the Base class
    attributes:
        __width, __height, __x, __y
    methodes:
        __init__
        area(self)
        display(self)
        __str__(self)
        update(self, *args)
        to_dictionary(self)
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """
        init func
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """getter"""
        return self.__width

    @property
    def height(self):
        """getter"""
        return self.__height

    @property
    def x(self):
        """getter"""
        return self.__x

    @property
    def y(self):
        """getter"""
        return self.__y

    @height.setter
    def height(self, value):
        """setter height"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @width.setter
    def width(self, value):
        """setter width"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @x.setter
    def x(self, value):
        """setter x"""
        if type(value) is not int:
            raise TypeError("x must be an integer")
        elif value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @y.setter
    def y(self, value):
        """setter y"""
        if type(value) is not int:
            raise TypeError("y must be an integer")
        elif value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """ function that return the area value of a rectangle"""
        return self.__width * self.__height

    def display(self):
        """
        function prints in stdout the Rectangle
        instance with the character #
        """
        print('\n' * self.__y + (
              ' ' * self.__x + '#' * self.width + '\n') * self.__height,
              end='')

    def __str__(self):
        """returns [Rectangle] (<id>) <x>/<y> - <width>/<height>"""
        return "[Rectangle] ({:d}) {:d}/{:d} - {:d}/{:d}\
                ".format(self.id, self.__x, self.__y, self.__width, self.__height)

    def update(self, *args, **kwargs):
        """
        method def update(self, *args): that assigns an argument to each attribute
        """
        funcs = ["id", "width", "height", "x", "y"]
        if args:
            for i in range(args):
                setattr(self, funcs[i], args[i])
        else:
            for k, v in kwargs.items():
                setattr(self, k, v)

    def to_dictionary(self):
        """
        A function that returns the dictionary presentation of an obj
        """
        dic = {}
        list_attrs = ['x', 'y', "id", "height", "width"]
        list_vals = [self.x, self.y, self.id, self.height, self.width]

        for k, v in zip(list_attrs, list_vals):
            dic[k] = v

        return dic
