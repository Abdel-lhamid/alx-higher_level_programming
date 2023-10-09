#!/usr/bin/python3
def max_integer(my_list=[]):
    if my_list:
        maxi = my_list[0]
        for i in max_integer:
            if i > maxi:
            maxi = i
        return maxi
    else:
        return None
