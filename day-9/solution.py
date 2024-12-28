class Block:
    TYPE_SPACE = 0
    TYPE_FILE = 1

    def __init__(self, block_type, files, space_length):
        self.block_type = block_type  # 0: space, 1: file
        self.files = files  # List of file IDs (or empty list for spaces)
        self.space_length = space_length  # Length of space (or 0 for files)


def parse_blocks(data):
    disk_map = data[0]  # Input disk map string
    blocks = []  # List of Block objects [block_type, [file_ids], space_length]

    block_type = Block.TYPE_FILE  # Start with files
    file_id = 0
    space_count = 0
    space_idx = []

    # Loop through the disk map string and process file blocks and spaces
    for i in map(int, disk_map):
        if block_type == Block.TYPE_FILE:
            block = Block(
                block_type=block_type,
                files=[file_id] * i,  # Create file blocks with the current file ID
                space_length=0,
            )
            blocks.append(block)
            file_id += 1
        else:
            if i > 0:
                space_count += i
                space_idx.append(len(blocks))
                block = Block(
                    block_type=block_type,
                    files=[],  # No files in space blocks
                    space_length=i,
                )
                blocks.append(block)
        block_type = (block_type + 1) % 2  # Alternate between space and file blocks

    return blocks, space_count, space_idx


def part1(data):
    blocks, space_count, space_idx = parse_blocks(data)

    # Initialize variables for the file compaction process
    curr_block = []  # Holds the current block of files to move
    curr_space_idx = space_idx.pop(0)  # First space index for compaction

    # Start moving files to the leftmost available space
    while space_count:
        if len(curr_block) == 0:
            # If no files to move, clean up empty space blocks
            if blocks[-1].block_type == Block.TYPE_SPACE and len(blocks[-1].files) == 0:
                blocks.pop()  # Remove empty space block
                space_idx.pop()
                continue

            if blocks[-1].block_type == Block.TYPE_FILE:
                curr_block = blocks.pop().files  # Get the next block of files to move

        try:
            item = curr_block.pop()  # Try to pop a file block
        except IndexError:
            break  # No more files to move

        # Place the file into the current space
        blocks[curr_space_idx].files.append(item)
        blocks[curr_space_idx].space_length -= 1
        space_count -= 1

        if blocks[curr_space_idx].space_length == 0:
            blocks[curr_space_idx].block_type = Block.TYPE_FILE  # Convert to file block
            if space_idx:
                curr_space_idx = space_idx.pop(0)  # Get the next space index
            else:
                break  # No more spaces

    # If there are leftover files, add them as new file blocks
    if curr_block:
        blocks.append(
            Block(
                block_type=Block.TYPE_FILE,
                files=curr_block,
                space_length=0,
            )
        )

    # Calculate the checksum by summing the positions of file blocks multiplied by their IDs
    checksum = 0
    pos = 0
    for block in blocks:
        for file in block.files:
            checksum += pos * file
            pos += 1

    return checksum


def part2(data):
    blocks, space_count, space_idx = parse_blocks(data)

    curr_block_idx = len(blocks) - 1

    while curr_block_idx > 0:
        if blocks[curr_block_idx].block_type == Block.TYPE_SPACE:
            curr_block_idx -= 1
            continue

        curr_block_len = len(blocks[curr_block_idx].files)
        for curr_space_idx in space_idx:
            if curr_space_idx >= curr_block_idx:
                break

            if blocks[curr_space_idx].space_length >= curr_block_len:
                blocks[curr_space_idx].files.extend(blocks[curr_block_idx].files)
                blocks[curr_space_idx].space_length -= curr_block_len

                blocks[curr_block_idx].block_type = Block.TYPE_SPACE
                blocks[curr_block_idx].space_length = curr_block_len
                blocks[curr_block_idx].files = []

                if blocks[curr_space_idx].space_length == 0:
                    space_idx.remove(curr_space_idx)

                break

        curr_block_idx -= 1

    checksum = 0
    pos = 0
    for block in blocks:
        for file in block.files:
            checksum += pos * file
            pos += 1
        if block.block_type == Block.TYPE_SPACE:
            pos += block.space_length

    return checksum


# Example usage:
filename = "day-9/input.txt"  # Replace with your actual input filename

# Read input from the file
with open(filename, "r") as file:
    data = [file.read().strip()]

# Call the part1 function and print the result
# result = part1(data)
result = part2(data)
print(f"Filesystem checksum: {result}")
