#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    new_list = my_list[:]
    for value in new_list:
        if value % 2 == 0:
            return True
        else:
            False
