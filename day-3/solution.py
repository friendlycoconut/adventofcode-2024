#!/bin/python3
import re


def task1(file_path):
    """
    Reads a file containing corrupted memory instructions, extracts valid `mul(X,Y)`
    instructions, and computes the sum of their results.
    """
    try:
        # Open and read the file content
        with open(file_path, "r") as file:
            memory = file.read()

        # Regular expression to match valid mul(X,Y) instructions
        pattern = r"mul\((\d{1,3}),(\d{1,3})\)"

        # Find all matches
        matches = re.findall(pattern, memory)

        # Compute the sum of all valid multiplications
        total = sum(int(x) * int(y) for x, y in matches)

        return total
    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found.")
        return None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None


def task2(file_path):
    """
    Reads a file containing corrupted memory instructions, handles `do()` and `don't()` conditions,
    extracts valid `mul(X,Y)` instructions, and computes the sum of results for enabled instructions.
    """
    try:
        # Open and read the file content
        with open(file_path, "r") as file:
            memory = file.read()

        # Regular expressions to match valid mul(X,Y), do(), and don't() instructions
        mul_pattern = r"mul\((\d{1,3}),(\d{1,3})\)"
        condition_pattern = r"(do\(\)|don't\(\))"

        # Find all mul instructions and conditional statements
        instructions = re.findall(rf"{mul_pattern}|{condition_pattern}", memory)

        # Variables to track current state and the sum of valid multiplications
        is_enabled = True  # mul instructions are initially enabled
        total = 0

        for match in instructions:
            if match[2]:  # A condition was matched (`do()` or `don't()`)
                condition = match[2]
                if condition == "do()":
                    is_enabled = True
                elif condition == "don't()":
                    is_enabled = False
            elif (
                is_enabled and match[0] and match[1]
            ):  # A valid mul(X,Y) was matched and is enabled
                x, y = int(match[0]), int(match[1])
                total += x * y

        return total
    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found.")
        return None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None


# Example usage
if __name__ == "__main__":
    file_path = "day-3/input.txt"  # Replace with your input file name
    result = task1(file_path)
    result = task2(file_path)
    if result is not None:
        print(f"The sum of valid `mul` instructions is: {result}")
