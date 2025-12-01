# https://adventofcode.com/2024/day/9

import pathlib
import time
from collections import deque


script_path = pathlib.Path(__file__).parent
soln_file = script_path / "input.txt"  # 6461289671426
test_file = script_path / "test.txt"  # 1928
test_file_x = script_path / "test_x.txt"  # 60


# 1766 test


def parse_block_gap_sequence(seq):
    """Parses a sequence of block and gap widths into a list of tuples.

    Args:
      sequence: A string representing the sequence of block and gap widths.

    Returns:
      A list of tuples, where each tuple contains the block width and gap width.
    """

    file_system = []
    fileID = 0

    for i, block in enumerate(seq):
        block_width = int(block)

        if i % 2 == 0:
            file_system.append((i, block_width, fileID))
            fileID += 1
            continue

        file_system.append((i, block_width, ""))

    return file_system


def parse(puzzle_input):
    """Parse input"""

    with open(puzzle_input, "r", encoding="UTF-8") as file:
        #  Read each line (split \n) and form a list of strings
        lst = parse_block_gap_sequence(file.read())

    return lst


def calculate_digit_sum(number):
    """Calculates the sum of the product of each digit and its position.

    Args:
      number: The input number as a string.

    Returns:
      The calculated sum.
    """

    digit_sum = 0
    position = 0
    for digit in number:
        digit_sum += int(digit) * position
        position += 1
    return digit_sum


# Example usage:
number = "0099811188827773336446555566"
result = calculate_digit_sum(number)
print(result)  # Output: 1928


def part1(data):
    """Solve part 1"""

    # pos on the line gets a number
    # if odd then its a file, even its a space/gap
    # the number and the type then show how long the file is or gap is

    # how to store this data, in numbers not strings
    # the files have id based on reading left to right, so need to assign
    # then need to tag the gaps with the right file, filling up left to right
    #    so reading the files backwards and filling in the gaps. reverse order?

    # in the structure, just need to read the id of the file (dont get hung up on 1 char or not. its ID)
    # and then assign that to the position (file bvlock)
    # or move it later into a gap, in order, based on reading from the end and filling gaps forwards

    # can we calcualte the answer as we go.

    # read FORWARD AND read backward?  when pos1 > pos2
    # dont know the ids..... so need to read once and assign IDs to all the file blocks
    # what to store, as the order is important

    # gaps might need to be split into 2 or more depending on if there are enough of a specific file to break down
    # list slices?  before, change, keep after, then repeat?

    print(data)

    working_filesystem = data.copy()
    queue = deque(working_filesystem)

    answer = []
    # Do I need to capture what final order is... part 2?

    final_pos = 0

    while queue:
        print("\nQ Len", len(queue))
        block_pos, block_width, block_id = queue.popleft()
        print("pos, width, block_id:", block_pos, block_width, block_id, "|")

        if block_pos is None:
            output = [(final_pos + c) * block_id for c in range(block_width)]
            print(output)
            answer.append(sum(output))
            break

        if block_id != "":
            output = [(final_pos + c) * block_id for c in range(block_width)]
            print(output)
            answer.append(sum(output))
            final_pos += block_width
        else:
            print("Gap width", block_width)
            gap_to_fill = block_width

            # careful = when pull gaps from end, need to just ignore? and pull again?

            while queue and gap_to_fill > 0:
                _, last_width, last_id = queue.pop()

                if last_width == 0 or last_id == "":
                    continue

                new_item_id = last_id

                # Last item is bigger than the gap
                # so there will be left over to add to the end of the queue
                if gap_to_fill <= last_width:
                    new_item_width = gap_to_fill
                    remainder = last_width - gap_to_fill
                    if remainder > 0:
                        queue.append((None, remainder, new_item_id))

                    gap_to_fill = 0
                else:
                    # Last item smaller the gap. So it fully fills it
                    # so there is left over space to fill with another file
                    new_item_width = last_width
                    remainder = 0  # NOT: gap_to_fill - last_width
                    gap_to_fill -= last_width
                    #  Nothing to add on to the end of the queue

                output = [(final_pos + c) * new_item_id for c in range(new_item_width)]
                print(output)
                answer.append(sum(output))
                final_pos += new_item_width

        # final_pos += block_width

        print("\nfinal-pos:", final_pos)

    print(answer)

    return sum(answer)


def part2(data):
    """Solve part 2"""

    return 1


def solve(puzzle_input, run="Solution"):
    """Solve the puzzle for the given input"""
    times = []

    data = parse(puzzle_input)

    times.append(time.perf_counter())
    solution1 = part1(data)
    times.append(time.perf_counter())
    solution2 = part2(data)
    times.append(time.perf_counter())

    print(f"{run} 1: {str(solution1)} in {times[1]-times[0]:.4f}s")
    print(f"{run} 2: {str(solution2)} in {times[2]-times[1]:.4f}s")
    print(f"\nExecution total: {times[-1]-times[0]:.4f} seconds")

    return solution1, solution2, times


if __name__ == "__main__":
    print("\nAOC")

    tests = solve(test_file_x, run="Test_x")

    tests = solve(test_file, run="Test")

    print()
    solutions = solve(soln_file)
