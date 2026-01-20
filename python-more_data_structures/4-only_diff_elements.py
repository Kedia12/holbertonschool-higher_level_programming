#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    set_3 = set()
    for value in set_1 and set_2:
        if value in set_1 == set_2:
            continue
        else:
            set_3.add(value)
            