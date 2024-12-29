from itertools import product
from collections import deque


def task1(filename):
    with open(filename, "r") as file:
        # Read input
        stones = list(
            map(int, file.readline().strip().split())
        )  # First line contains stones
        blinks = int(file.readline().strip())  # Second line contains number of blinks

    # Process each blink
    for _ in range(blinks):
        new_stones = []
        for stone in stones:
            if stone == 0:
                new_stones.append(1)
            elif len(str(stone)) % 2 == 0:  # Even number of digits
                mid = len(str(stone)) // 2
                left, right = str(stone)[:mid], str(stone)[mid:]
                new_stones.append(int(left))
                new_stones.append(int(right))
            else:
                new_stones.append(stone * 2024)
        stones = new_stones

    # Output the result
    return len(stones)


def task2(filename): ...


if __name__ == "__main__":
    filename = "day-11/input.txt"

    result = task1(filename)
    print(result)
    result = task2(filename)
    print(result)
