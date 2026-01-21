#!/usr/bin/python3
def best_score(a_dictionary):
    if not a_dictionary:
        return None
    best_key = None
    best_value = None
    for key in a_dictionary:
        if best_value is None:
            best_value = a_dictionary[key]
            best_key = key
        else:
            if a_dictionary[key] > best_value:
                best_value = a_dictionary[key]
                best_key = key
    return best_key
