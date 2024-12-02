# https://adventofcode.com/2024/day/2

import pathlib
import time

script_path = pathlib.Path(__file__).parent
soln_file = script_path / "input.txt"  # 549 / 
test_file = script_path / "test.txt"  # 2 / 

def convert_to_numbers(list_of_lists):
    """Converts a list of list of strings into a list of list of integers.

    Args:
        list_of_lists: A list of list of strings.

    Returns:
        A list of list of numbers.
    """
    return [[int(s) for s in inner_list] for inner_list in list_of_lists]


def parse(puzzle_input):
    """Parse input"""

    with open(puzzle_input, "r", encoding="UTF-8") as file:
        #  Read each line (split \n) and form a list of strings
        lst = convert_to_numbers([x.split(" ") for x in file.read().split("\n")])

    return lst


def part1(data):
    """Solve part 1"""

    safe_list = []
    safe_count = 0

    for l in data:
        print("\n",l)
        dir = 1 if l[0] > l[-1] else -1
       
        a = l[0]
        still_safe = False

        for n in range(1,len(l)):

            cur_dir = 1 if l[n] < l[n-1] else -1
            if cur_dir != dir:
                print("Direction unsafe", cur_dir, dir)
                still_safe = False
                break

            b = l[n]
            print(n, ":", a, b, (a - b) * dir)

            if 0 < (a - b) * dir <= 3:
                still_safe = True
            else:
                print("Difference unsafe")
                still_safe = False
                break

            a = b

        if still_safe:
            safe_list.append(l)
            safe_count += 1


    print(safe_count)
    print(safe_list)

    return safe_count


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

    tests = solve(test_file, run="Test")

    print()
    solutions = solve(soln_file)
