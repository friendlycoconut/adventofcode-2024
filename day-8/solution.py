from itertools import product
from collections import defaultdict


def task1(filename):
    # Read the file data
    with open(filename, "r") as file:
        data = file.read().splitlines()

    # Create a grid of the map
    _map = [list(line) for line in data]
    rows, cols = len(_map), len(_map[0])

    # Create a dictionary to store the positions of each antenna by frequency
    antennas = defaultdict(list)

    # Loop through the grid and record the positions of the antennas
    for row in range(rows):
        for col in range(cols):
            if _map[row][col] != ".":
                antennas[_map[row][col]].append((row, col))

    # Set to keep track of unique antinode locations
    antinodes = set()

    # Process each frequency and calculate the antinodes
    for antenna, coords in antennas.items():
        # Compare each pair of antennas of the same frequency
        for i in range(len(coords)):
            for j in range(i + 1, len(coords)):
                # Calculate the difference in positions between the two antennas
                diff = tuple(a - b for a, b in zip(coords[j], coords[i]))

                # Try to find antinodes in both directions
                for _idx, _dir in [(i, -1), (j, 1)]:
                    # Calculate the antinode position based on the difference
                    pos = tuple([a + b * _dir for a, b in zip(coords[_idx], diff)])
                    # Ensure the position is within bounds of the map
                    if 0 <= pos[0] < rows and 0 <= pos[1] < cols:
                        antinodes.add(pos)

    # Return the number of unique antinode locations
    return len(antinodes)


def task2(filename): ...


if __name__ == "__main__":
    filename = "day-8/input.txt"

    result = task1(filename)
    print(result)
    result = task2(filename)
    print(result)
