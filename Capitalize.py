#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the solve function below.
def solve(s):
    if 0 < len(s) <1000:
        names = s.split(" ")
        caps_name = ""
        for _ in names:
            if _ == " ":
                caps_name += " "
            caps_name += _[0:1].upper()+_[1:]+" "
        return caps_name.strip()

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)

    fptr.write(result + '\n')

    fptr.close()