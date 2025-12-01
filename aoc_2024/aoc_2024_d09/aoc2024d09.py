# https://adventofcode.com/2024/day/9

import pathlib
import time
from collections import deque


script_path = pathlib.Path(__file__).parent
soln_file = script_path / "input.txt"  # 6461289671426
test_file = script_path / "test.txt"  # 1928 / 2858
test_file_x = script_path / "test_x.txt"  # 60


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
# number = "0099811188827773336446555566"
# result = calculate_digit_sum(number)
# print(result)  # Output: 1928


def part1(data):
    """Solve part 1"""
    print(data)

    working_filesystem = data.copy()
    queue = deque(working_filesystem)

    answer = []
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

    # print(answer)

    return sum(answer)


def part2(data):
    """Solve part 2"""

    working_filesystem = data.copy()
    queue = deque(working_filesystem)

    answer = []
    final_pos = 0

    while queue:
        print("\nQ Len", len(queue))

        block_pos, block_width, block_id = queue.popleft()
        print("pos, width, block_id:", block_pos, block_width, block_id, "|")

        # if block_pos is None:
        #     output = [(final_pos + c) * block_id for c in range(block_width)]
        #     print(output)
        #     answer.append(sum(output))
        #     break

        if block_id != "":
            block_sum = [(final_pos + c) * block_id for c in range(block_width)]
            print(block_sum)
            answer.append(sum(block_sum))
            final_pos += block_width

        else:
            # Process a gap
            print("Gap width", block_width)
            gap_width = block_width
            found_block = False

            # Iterate through the remaining blocks in reverse order
            for i in range(len(queue) - 1, -1, -1):
                last_pos, last_width, last_id = queue[i]
                print(last_pos, last_width, last_id)

                if last_id:  # Skip gaps at the end of the queue
                    if last_width == gap_width:
                        # Perfect match, remove the block and fill the gap
                        queue.remove((last_pos, last_width, last_id))
                        block_sum = sum(
                            (final_pos + j) * last_id for j in range(last_width)
                        )
                        answer.append(block_sum)
                        final_pos += last_width
                        found_block = True
                        break
                    elif last_width < gap_width:
                        # Partial match, remove the block and reduce the gap
                        queue.remove((last_pos, last_width, last_id))
                        block_sum = sum(
                            (final_pos + j) * last_id for j in range(last_width)
                        )
                        answer.append(block_sum)
                        final_pos += last_width
                        gap_width -= last_width

                    if not found_block:
                        # Gap couldn't be fully filled, add the remaining gap to the front of the queue
                        queue.appendleft((final_pos, gap_width, ""))
                        # need to remove if moved
                        #  need to tag if already TRIED
                        # ÷ need add a gap left
                        break

    # print(answer)
    print(sum(answer))
    return -1


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

    # tests = solve(test_file_x, run="Test_x")

    tests = solve(test_file, run="Test")

    print()
    # solutions = solve(soln_file)
