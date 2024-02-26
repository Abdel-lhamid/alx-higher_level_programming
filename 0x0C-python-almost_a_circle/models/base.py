#!/usr/bin/python3
"""
    Model 01 Base Class
    contains the base CLass
"""
import json
import os
import csv
import turtle


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
            save_to_file_csv(cls, list_objs)
            load_from_file_csv(cls)
            draw(list_rectangles, list_squares)
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

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """
        method that saves list to csv file
        """
        filename = cls.__name__ + ".csv"
        with open(filename, 'w', newline='') as f:
            writer = csv.writer(f)
            for ob in list_objs:
                if cls.__name__ == "Rectangle":
                    writer.writerow([ob.id, ob.width, ob.height, ob.x, ob.y])
                if cls.__name__ == "Square":
                    writer.writerow([ob.id, ob.size, ob.x, ob.y])

    @classmethod
    def load_from_file_csv(cls):
        """
        method that reads from csv file
        """
        list_objs = []
        filename = cls.__name__ + ".csv"
        with open(filename, 'r', newline='') as f:
            reader = csv.reader(f)
            for row in reader:
                if cls.__name__ == "Rectangle":
                    dic = {"id": int(row[0]),
                           "width": int(row[1]),
                           "height": int(row[2]),
                           "x": int(row[3]),
                           "y": int(row[4])}
                if cls.__name__ == "Square":
                    dic = {"id": int(row[0]),
                           "size": int(row[1]),
                           "x": int(row[2]),
                           "y": int(row[3])}
                obj = cls.create(**dic)
                list_objs.append(obj)
        return list_objs

    @staticmethod
    def draw(list_rectangles, list_squares):
        """
        hat opens a window and draws all the Rectangles and Squares
        """

        screen = turtle.Screen()
        screen.title("Drawing Rectangles and Squares")
        screen.bgcolor("white")

        pen = turtle.Turtle()
        pen.speed(2)

        for rectangle in list_rectangles:
            pen.penup()
            pen.goto(rectangle.x, rectangle.y)
            pen.pendown()
            pen.color("blue")  # You can customize the color
            pen.begin_fill()
            for _ in range(2):
                pen.forward(rectangle.width)
                pen.left(90)
                pen.forward(rectangle.height)
                pen.left(90)
            pen.end_fill()

        for square in list_squares:
            pen.penup()
            pen.goto(square.x, square.y)
            pen.pendown()
            pen.color("red")  # You can customize the color
            pen.begin_fill()
            for _ in range(4):
                pen.forward(square.size)
                pen.left(90)
            pen.end_fill()

        screen.mainloop()
