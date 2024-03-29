#!/usr/bin/python3
"""
Module 7-rectangle
Contains class Rectangle with private attribute width and height,
public area and perimeter methods, and allows printing, and delete
"""


class Rectangle:
    """
    Class Rectangle with attrs width and height
    """
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """init rect"""
        self.width = width
        self.height = height
        type(self).number_of_instances += 1

    @property
    def width(self):
        """getter for width"""
        return self.width

    @width.setter
    def width(self, value):
        """setter for width"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """ Getter for height """
        return self.__height

    @height.setter
    def height(self, value):
        """ Setter for height if int > 0 """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """ Return width * height """
        return self.__width * self.__height

    def perimeter(self):
        """ Return 2*width + 2*height (or return 0 if width or height is 0)"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return (2 * self.__width) + (2 * self.height)

    def __str__(self):
        """ Prints rectangle with print symbol """
        if self.__width == 0 or self.__height == 0:
            return ""
        pic = "\n".join([str(self.print_symbol) * self.__width
                         for rows in range(self.__height)])
        return pic

    def __repr__(self):
        """ String representation to recreate new instance """
        return "Rectangle({:d}, {:d})".format(self.__width, self.__height)

    def __del__(self):
        """prints after deletion of an intence of class"""
        print("Bye rectangle...")
        type(self).number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """evaluate 2 rectang and prints message"""
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return rect_1
        return rect_2
