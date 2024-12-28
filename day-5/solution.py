def task1(filename):
    # Read input from file
    with open(filename, "r") as file:
        sections = file.read().split("\n\n")

    # Parse rules
    rules = []
    for line in sections[0].strip().splitlines():
        x, y = map(int, line.split("|"))
        rules.append((x, y))

    # Parse updates
    updates = []
    for line in sections[1].strip().splitlines():
        updates.append(list(map(int, line.split(","))))

    # Validate updates
    def is_valid(update):
        """Check if an update follows all the ordering rules."""
        position = {page: i for i, page in enumerate(update)}  # Map page -> position
        for x, y in rules:
            if (
                x in position and y in position
            ):  # Rule applies only if both pages exist in update
                if position[x] > position[y]:  # Check if x comes before y
                    return False
        return True

    # Process updates and calculate the result
    valid_sum = 0
    for update in updates:
        if is_valid(update):
            middle = update[len(update) // 2]  # Find the middle page
            valid_sum += middle

    return valid_sum


def task2(filename):
    """Fix invalid updates based on rules and sum the middle page numbers."""
    # Read input file
    with open(filename, "r") as file:
        sections = file.read().split("\n\n")

    # Parse rules
    rules = []
    for line in sections[0].strip().splitlines():
        x, y = map(int, line.split("|"))
        rules.append((x, y))

    # Parse updates
    updates = []
    for line in sections[1].strip().splitlines():
        updates.append(list(map(int, line.split(","))))

    # Create a graph of dependencies based on rules
    from collections import defaultdict, deque

    graph = defaultdict(list)  # Directed graph
    in_degree = defaultdict(int)  # Track incoming edges for topological sort

    # Build the graph and in-degrees
    for x, y in rules:
        graph[x].append(y)
        in_degree[y] += 1
        if x not in in_degree:
            in_degree[x] = 0

    # Topological sorting function for ordering updates
    def sort_pages(pages):
        """Sort pages based on dependency rules using topological sorting."""
        # Filter graph for only relevant pages in the update
        local_graph = defaultdict(list)
        local_in_degree = {page: 0 for page in pages}

        for x, y in rules:
            if x in pages and y in pages:
                local_graph[x].append(y)
                local_in_degree[y] += 1

        # Perform topological sort
        queue = deque([node for node in pages if local_in_degree[node] == 0])
        sorted_pages = []
        while queue:
            node = queue.popleft()
            sorted_pages.append(node)
            for neighbor in local_graph[node]:
                local_in_degree[neighbor] -= 1
                if local_in_degree[neighbor] == 0:
                    queue.append(neighbor)

        return sorted_pages

    # Validation function to check ordering
    def is_valid(update):
        """Check if an update satisfies all rules."""
        position = {page: i for i, page in enumerate(update)}
        for x, y in rules:
            if x in position and y in position and position[x] > position[y]:
                return False
        return True

    # Process updates
    invalid_sum = 0
    for update in updates:
        if not is_valid(update):  # Only process invalid updates
            fixed_update = sort_pages(update)  # Fix the order using topological sort
            middle = fixed_update[len(fixed_update) // 2]  # Find middle page
            invalid_sum += middle  # Add to sum

    return invalid_sum


if __name__ == "__main__":
    file_path = "day-5/input.txt"  # Replace with your input file name
    result = task1(file_path)
    result = task2(file_path)

    print(result)
