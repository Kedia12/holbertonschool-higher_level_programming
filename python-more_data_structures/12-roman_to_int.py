#!/usr/bin/python3
def roman_to_int(roman_string):
    if roman_string is None or not isinstance(roman_string, str):
        return 0
    roman_string = roman_string.upper()
    values = {'I': 1, 'V': 5, 'X': 10, 'L': 50,
              'C': 100, 'D': 500, 'M': 1000}
    total = 0
    i = 0
    while i < len(roman_string):
        if roman_string[i] not in values:
            return 0
        curr = values[roman_string[i]]
        if i + 1 < len(roman_string):
            if roman_string[i + 1] not in values:
                return 0
            nxt = values[roman_string[i + 1]]
            if curr < nxt:
                total += (nxt - curr)
                i += 2
                continue
        total += curr
        i += 1
    return total
