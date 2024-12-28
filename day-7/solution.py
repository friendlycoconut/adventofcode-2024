from itertools import product


def task1(filename):
    with open(filename, "r") as file:
        total = 0  # Total calibration result

        for line in file:  # Process each line in the input file
            # Parse target value and the list of numbers
            target, values = line.split(": ")
            target = int(target)
            values = list(map(int, values.split()))

            # Generate all possible operator combinations
            for ops in product(["+", "*"], repeat=len(values) - 1):
                # Evaluate expression left-to-right
                result = values[0]
                for i in range(len(ops)):
                    result = (
                        result + values[i + 1]
                        if ops[i] == "+"
                        else result * values[i + 1]
                    )

                # Check if the result matches the target
                if result == target:
                    total += target
                    break  # Stop after the first valid match

        return total  # Return the total calibration result


def task2(filename):
    with open(filename, "r") as file:
        total = 0  # Total calibration result

        for line in file:  # Process each line in the input file
            # Parse target value and the list of numbers
            target, values = line.split(": ")
            target = int(target)
            values = list(map(int, values.split()))

            # Generate all possible operator combinations (+, *, ||)
            for ops in product(["+", "*", "||"], repeat=len(values) - 1):
                # Evaluate expression left-to-right
                result = values[0]
                valid = True  # Assume valid unless proven otherwise

                for i in range(len(ops)):
                    if ops[i] == "+":
                        result += values[i + 1]
                    elif ops[i] == "*":
                        result *= values[i + 1]
                    elif ops[i] == "||":
                        # Concatenate by converting to string and back to integer
                        result = int(str(result) + str(values[i + 1]))

                    # If result exceeds target early, no need to continue
                    if result > target:
                        valid = False
                        break

                # Check if the result matches the target
                if valid and result == target:
                    total += target
                    break  # Stop after the first valid match

        return total  # Return the total calibration result


if __name__ == "__main__":
    filename = "day-7/input.txt"

    result = task1(filename)
    print(result)
    result = task2(filename)
    print(result)
