#!/usr/bin/python3
"""
    Module 100 append_after
    funcs:
            append_after(filename="", search_string="", new_string="")
"""


def append_after(filename="", search_string="", new_string=""):
    """
    a function that inserts a line of text to a file,
    after each line containing a specific string
    Attrs:
        filename: the file name
        search_string: the string to append after
        new_string: the string to insert
    """
    lines_to_append = []

    with open(filename, 'r') as file:
        lines = file.readlines()

        for line in lines:
            lines_to_append.append(line)
            if search_string in line:
                lines_to_append.append(new_string)

    with open(filename, 'w') as file:
        file.writelines(lines_to_append)
