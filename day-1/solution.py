#!/bin/python3

def task1(filename):
    file = open(filename, "r")

    column_1 = []
    column_2 = []
    result = 0

    lines = file.readlines()
    for x in lines:
        column_1.append(x.split("   ")[0])
        column_2.append(x.split("   ")[1])

    column_1.sort()
    column_2.sort()

    for i, x in enumerate(column_1):
        result += abs(int(column_2[i]) - int(x))

    return result


def task2(filename):
    file = open(filename, "r")

    column_1 = []
    column_2 = []
    res = 0

    lines = file.readlines()
    for x in lines:
        column_1.append(int(x.split("   ")[0]))
        column_2.append(int(x.split("   ")[1]))

    for x in column_1:
        res += int(x) * (column_2.count(int(x)))

    return res


if __name__ == "__main__":
    res = task1("day-1/input.txt")
    print(res)
    res = task2("day-1/input.txt")
    print(res)
