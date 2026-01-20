#!/usr/bin/python3
def uniq_add(my_list=[]):
    result = 0
    search = []
    for value in my_list:
        if value not in search:
            search.append(value)
            result += value
    return result
