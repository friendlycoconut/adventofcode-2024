from itertools import product
from collections import deque


def task1(filename):
    # Read the input map from the file
    with open(filename, "r") as file:
        map_data = [list(map(int, line.strip())) for line in file]

    # Helper function to perform BFS and count reachable 9s
    def bfs(map_data, start_row, start_col):
        rows, cols = len(map_data), len(map_data[0])
        queue = deque([(start_row, start_col)])  # Start at the trailhead
        visited = set()
        visited.add((start_row, start_col))

        reachable_9s = 0

        # Directions: up, down, left, right
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        while queue:
            row, col = queue.popleft()

            # If we reach a height of 9, increment the count
            if map_data[row][col] == 9:
                reachable_9s += 1

            # Explore neighbors
            for dr, dc in directions:
                new_row, new_col = row + dr, col + dc

                # Check if the new position is within bounds
                if 0 <= new_row < rows and 0 <= new_col < cols:
                    # Check if we can move to the next tile (height + 1)
                    if (new_row, new_col) not in visited and map_data[new_row][
                        new_col
                    ] == map_data[row][col] + 1:
                        visited.add((new_row, new_col))
                        queue.append((new_row, new_col))

        return reachable_9s

    # Variables to store the sum of scores
    rows, cols = len(map_data), len(map_data[0])
    trailhead_scores = 0

    # Loop over the map to find all trailheads (positions with height 0)
    for row in range(rows):
        for col in range(cols):
            if map_data[row][col] == 0:
                # For each trailhead, perform BFS/DFS to find reachable 9s
                score = bfs(map_data, row, col)
                trailhead_scores += score

    return trailhead_scores


def task2(filename):
    with open(filename, "r") as f:
        data = f.read().strip().splitlines()
    # Convert input data into a 2D map of integers
    _map = [list(map(int, line)) for line in data]
    rows, cols = len(_map), len(_map[0])

    # Directions for moving up, down, left, right
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    # Helper function to explore and find the distinct trails from a trailhead
    def get_score(start_row, start_col):
        queue = deque([(start_row, start_col)])  # Start at the trailhead
        visited = set()
        visited.add((start_row, start_col))

        # Track all the distinct trails leading to a 9
        distinct_trails = set()

        while queue:
            row, col = queue.popleft()

            # If we reach a height of 9, record the trail
            if _map[row][col] == 9:
                distinct_trails.add((row, col))

            # Explore neighbors
            for dr, dc in directions:
                new_row, new_col = row + dr, col + dc

                # Check if the new position is within bounds
                if 0 <= new_row < rows and 0 <= new_col < cols:
                    # Check if we can move to the next tile (height + 1)
                    if (new_row, new_col) not in visited and _map[new_row][
                        new_col
                    ] == _map[row][col] + 1:
                        visited.add((new_row, new_col))
                        queue.append((new_row, new_col))

        return distinct_trails

    score = 0

    # Traverse the map and find all trailheads (height 0)
    for i in range(rows):
        for j in range(cols):
            if _map[i][j] == 0:
                # Get the score for each trailhead
                endpoints = get_score(i, j)
                score += len(endpoints)

    return score


if __name__ == "__main__":
    filename = "day-10/input.txt"

    result = task1(filename)
    print(result)
    result = task2(filename)
    print(result)
