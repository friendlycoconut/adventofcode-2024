def task1(filename):
    # Read the input map
    with open(filename, "r") as file:
        grid = [list(line.strip()) for line in file.readlines()]

    # Directions: [Up, Right, Down, Left]
    directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]  # (dy, dx)
    # Map symbols to starting directions
    dir_map = {"^": 0, ">": 1, "v": 2, "<": 3}

    # Find the guard's initial position and direction
    rows, cols = len(grid), len(grid[0])
    guard_pos = None
    direction = None

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] in dir_map:
                guard_pos = (r, c)
                direction = dir_map[grid[r][c]]
                grid[r][c] = "."  # Clear the guard's symbol from the grid
                break
        if guard_pos:
            break

    # Track visited positions
    visited = set()
    visited.add(guard_pos)  # Include the starting position

    # Simulate the guard's movement
    while True:
        # Calculate the next position
        dy, dx = directions[direction]
        nr, nc = guard_pos[0] + dy, guard_pos[1] + dx

        # Check if the guard leaves the map
        if nr < 0 or nr >= rows or nc < 0 or nc >= cols:
            break  # Exit the loop when leaving the map

        # Check for obstacles
        if grid[nr][nc] == "#":
            # Turn right (change direction)
            direction = (direction + 1) % 4
        else:
            # Move forward and mark visited
            guard_pos = (nr, nc)
            visited.add(guard_pos)

    # Return the total number of distinct positions visited
    return len(visited)


def task2(filename):
    # Read input from the file
    with open(filename, "r") as file:
        grid = [list(line.strip()) for line in file.readlines()]

    # Define directions and their mappings
    directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    dir_map = {"^": 0, ">": 1, "v": 2, "<": 3}

    # Locate the guard's position and direction
    rows, cols = len(grid), len(grid[0])
    guard_pos = None
    direction = None
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] in dir_map:
                guard_pos = (r, c)
                direction = dir_map[grid[r][c]]
                grid[r][c] = "."  # Clear guard's symbol from the grid
                break
        if guard_pos:
            break

    # Simulate the guard's path
    def simulate_path(start_pos, start_dir, obstacle=None):
        pos = start_pos
        dir_idx = start_dir
        visited = set()
        visited.add(pos)

        while True:
            # Compute next position
            dr, dc = directions[dir_idx]
            nr, nc = pos[0] + dr, pos[1] + dc

            # Check if guard leaves the grid
            if nr < 0 or nr >= rows or nc < 0 or nc >= cols:
                return visited, False  # Guard exits the map

            # Apply a new obstacle if specified
            if obstacle == (nr, nc):
                grid[nr][nc] = "#"

            # Check if obstacle is hit
            if grid[nr][nc] == "#":
                dir_idx = (dir_idx + 1) % 4  # Turn right 90 degrees
            else:
                pos = (nr, nc)
                if pos in visited:  # Loop detected
                    return visited, True
                visited.add(pos)

    # Simulate the guard's original path
    original_path, _ = simulate_path(guard_pos, direction)

    # Find valid positions for new obstructions
    loop_positions = set()
    for r in range(rows):
        for c in range(cols):
            # Ignore guard's starting position and obstacles
            if (r, c) != guard_pos and grid[r][c] == ".":
                _, is_loop = simulate_path(guard_pos, direction, (r, c))
                if is_loop:
                    loop_positions.add((r, c))

    # Return the number of valid positions for obstruction
    return len(loop_positions)


if __name__ == "__main__":
    filename = "day-6/input.txt"

    result = task1(filename)
    result = task2(filename)
    print(result)
