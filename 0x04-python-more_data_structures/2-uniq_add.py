#!/usr/bin/python3
def uniq_add(my_list=[]):
    summ = 0
    for i in set(my_list):
        summ += i
    return summ
