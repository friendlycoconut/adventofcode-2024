#!/bin/python3

import math
import os
import random
import re
import sys
 

def fileReader(filename):
    file = open(filename, "r")

    column_1 = []
    column_2 = []
    result = 0

    lines = file.readlines()
    for x in lines:
        column_1.append(x.split('   ')[0])
        column_2.append(x.split('   ')[1])

    column_1.sort()
    column_2.sort()

    for i,x in enumerate(column_1):
        result += abs(int(column_2[i])-int(x))

    return result    


if __name__ == '__main__':
    x = open("day-1/input.txt")
    print(x)
    res = fileReader("day-1/input.txt")
    print(res)