#!/usr/bin/python3
"""
    Module 07 add_item
    adds and save a python obj to a Json file
"""

from sys import argv
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file
f_name = "add_item.json"

try:
    content = load_from_json_file(f_name)
except FileNotFoundError:
    content = []

save_to_json_file(content + argv[1:], f_name)
