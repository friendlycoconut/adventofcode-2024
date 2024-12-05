def task1(file_path):
    """
    Reads a word search grid from a file and counts all occurrences of the word 'XMAS'
    in all possible directions.

    Parameters:
    file_path (str): Path to the input text file containing the word search grid.

    Returns:
    int: Total number of times 'XMAS' appears in all directions.
    """
    word = "XMAS"
    directions = [
        (0, 1),  # Right
        (0, -1),  # Left
        (1, 0),  # Down
        (-1, 0),  # Up
        (1, 1),  # Diagonal Down-Right
        (1, -1),  # Diagonal Down-Left
        (-1, 1),  # Diagonal Up-Right
        (-1, -1),  # Diagonal Up-Left
    ]

    try:
        # Read the grid from the file
        with open(file_path, "r") as file:
            grid = [line.strip() for line in file.readlines()]

        rows = len(grid)
        cols = len(grid[0])
        word_length = len(word)

        def is_valid_position(x, y):
            return 0 <= x < rows and 0 <= y < cols

        def count_word_from(x, y, dx, dy):
            """
            Counts if the word appears starting at position (x, y) in direction (dx, dy).
            """
            for i in range(word_length):
                nx, ny = x + i * dx, y + i * dy
                if not is_valid_position(nx, ny) or grid[nx][ny] != word[i]:
                    return 0
            return 1  # Word is found

        total_count = 0
        for i in range(rows):
            for j in range(cols):
                for dx, dy in directions:
                    total_count += count_word_from(i, j, dx, dy)

        return total_count
    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found.")
        return None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None


def count_xmas_patterns(grid):
    rows = len(grid)
    cols = len(grid[0])
    count = 0

    # Define all valid X-MAS patterns
    valid_mas = ["MAS", "SAM"]  # MAS forwards and backwards

    # Iterate through each potential 3x3 region in the grid
    for i in range(rows - 2):  # Stop 2 rows before the end
        for j in range(cols - 2):  # Stop 2 columns before the end
            # Extract the characters in the 3x3 region
            top_row = grid[i][j : j + 3]
            middle = grid[i + 1][j + 1]
            bottom_row = grid[i + 2][j : j + 3]

            # Check for the X-MAS pattern
            if (
                top_row in valid_mas  # Top MAS
                and bottom_row in valid_mas  # Bottom MAS
                and middle == "A"  # Center A
            ):
                count += 1

    return count


# Example usage
if __name__ == "__main__":
    file_path = "day-4/input.txt"  # Replace with your input file name
    result = task1(file_path)

    if result is not None:
        print(f"The word 'XMAS' appears {result} times.")

    with open("day-4/input.txt", "r") as file:
        grid = [line.strip() for line in file.readlines()]

    result = count_xmas_patterns(grid)
    print(f"Total X-MAS patterns: {result}")
