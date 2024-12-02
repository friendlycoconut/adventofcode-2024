#!/bin/python3
from itertools import cycle


def task1(file_path):
    def is_safe(report):
        # Convert the report (line) into a list of integers
        levels = list(map(int, report.split()))

        # Determine if the sequence is increasing or decreasing
        is_increasing = all(levels[i] < levels[i + 1] for i in range(len(levels) - 1))
        is_decreasing = all(levels[i] > levels[i + 1] for i in range(len(levels) - 1))

        if not (is_increasing or is_decreasing):
            return False  # Not all increasing or all decreasing

        # Check differences between adjacent levels
        for i in range(len(levels) - 1):
            diff = abs(levels[i] - levels[i + 1])
            if diff < 1 or diff > 3:
                return False  # Adjacent levels differ by less than 1 or more than 3

        return True

    # Read the file and process each line as a report
    with open(file_path, "r") as file:
        reports = file.readlines()

    # Count reports that are safe
    return sum(is_safe(report.strip()) for report in reports)


def task2(filename):

    def is_safe_dampener(report):
        def is_safe(levels):
            # Check if the levels are strictly increasing or strictly decreasing
            is_increasing = all(
                levels[i] < levels[i + 1] for i in range(len(levels) - 1)
            )
            is_decreasing = all(
                levels[i] > levels[i + 1] for i in range(len(levels) - 1)
            )

            if not (is_increasing or is_decreasing):
                return False

            # Check adjacent differences
            return all(
                1 <= abs(levels[i] - levels[i + 1]) <= 3 for i in range(len(levels) - 1)
            )

        levels = list(map(int, report.split()))

        # Check if the report is safe without removing any levels
        if is_safe(levels):
            return True

        # Try removing one level at a time and check if it becomes safe
        for i in range(len(levels)):
            modified_levels = levels[:i] + levels[i + 1 :]  # Remove the i-th level
            if is_safe(modified_levels):
                return True

        return False

    with open(filename, "r") as file:
        reports = file.readlines()

    return sum(is_safe_dampener(report.strip()) for report in reports)


if __name__ == "__main__":
    res = task1("day-2/input.txt")
    print(res)
    res = task2("day-2/input.txt")
    print(res)
