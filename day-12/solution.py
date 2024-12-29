from itertools import product
from collections import deque


def task1(filename):
    # Read the map data from the given file
    with open(filename, "r") as f:
        data = f.read().strip().splitlines()

    # Convert input data into a 2D map of characters
    _map = [list(line) for line in data]
    rows, cols = len(_map), len(_map[0])

    # Directions for moving up, down, left, right
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    # Helper function to explore and find a region from a starting position
    def explore_region(start_row, start_col):
        # Use BFS to explore the connected region
        queue = deque([(start_row, start_col)])
        region = set([(start_row, start_col)])
        plant_type = _map[start_row][start_col]

        while queue:
            row, col = queue.popleft()
            for dr, dc in directions:
                new_row, new_col = row + dr, col + dc
                if 0 <= new_row < rows and 0 <= new_col < cols:
                    if (new_row, new_col) not in region and _map[new_row][
                        new_col
                    ] == plant_type:
                        region.add((new_row, new_col))
                        queue.append((new_row, new_col))

        return region

    # Function to calculate the perimeter of a region
    def calculate_perimeter(region):
        perimeter = 0
        for row, col in region:
            for dr, dc in directions:
                new_row, new_col = row + dr, col + dc
                # If the neighbor is outside the map or a different plant type
                if (
                    not (0 <= new_row < rows and 0 <= new_col < cols)
                    or _map[new_row][new_col] != _map[row][col]
                ):
                    perimeter += 1
        return perimeter

    # Now, traverse the map to find all regions
    visited = set()
    total_price = 0

    for i in range(rows):
        for j in range(cols):
            if (i, j) not in visited:
                # Explore the region starting from this cell
                region = explore_region(i, j)
                # Mark the region cells as visited
                visited.update(region)
                # Calculate the area (size of the region)
                area = len(region)
                # Calculate the perimeter of the region
                perimeter = calculate_perimeter(region)
                # Calculate the price for the region and add it to the total price
                price = area * perimeter
                total_price += price

    return total_price


def task2(filename): ...


if __name__ == "__main__":
    filename = "day-12/input.txt"

    result = task1(filename)
    print(result)
    result = task2(filename)
    print(result)
