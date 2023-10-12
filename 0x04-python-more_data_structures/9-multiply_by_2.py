#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    if a_dictionary:
        mul_dic = {key: value * 2 for key, value in a_dictionary.items()}
    return mul_dic           
