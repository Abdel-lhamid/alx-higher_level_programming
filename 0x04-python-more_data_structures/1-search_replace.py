#!/usr/bin/python3
def search_replace(my_list, search, replace):
    if my_list is not None:
        n_list = my_list[:]
        n_list = list(map(lambda x: replace if x == search else x, n_list))
    return n_list
