#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    new_list = []
    for value in my_list:
        new_list.append(value % 2 == 0)
    return new_list
