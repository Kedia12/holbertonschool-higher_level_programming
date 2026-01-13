#!/usr/bin/python3
import sys
if __name__ == "__main__":
    total = 0
    for arg in sys.arg[:1]:
        total += int(arg)
    print(total)
