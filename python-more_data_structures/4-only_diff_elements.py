#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    set_3 = set()
    for value in set_1:
        if value not in set_2:
            set_3.add(value)
    return set_3
