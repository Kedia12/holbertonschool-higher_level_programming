#!/usr/bin/python3
def common_elements(set_1, set_2):
    set = []
    for value in set_1 and set_2:
        if value in set_1 and set_2:
            set.append(value)
    return set
