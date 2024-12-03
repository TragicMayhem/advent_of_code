# https://adventofcode.com/2024/day/2

import pathlib
import time

script_path = pathlib.Path(__file__).parent
soln_file = script_path / "input.txt"  # 549 /  589    (Not 579, 575 too low)
test_file = script_path / "test.txt"  # 2 / 4
test_file2 = script_path / "test2.txt"  #


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
        seq_dir = 1 if l[0] > l[-1] else -1

        a = l[0]
        still_safe = False

        for n in range(1, len(l)):

            cur_dir = 1 if l[n] < l[n - 1] else -1
            if cur_dir != seq_dir:
                # print("Direction unsafe", cur_dir, seq_dir)
                still_safe = False
                break

            b = l[n]
            # print(n, ":", a, b, (a - b) * seq_dir)

            if 0 < (a - b) * seq_dir <= 3:
                still_safe = True
            else:
                # print("Difference unsafe")
                still_safe = False
                break

            a = b

        if still_safe:
            safe_list.append(l)
            safe_count += 1

    # print(safe_count)
    # print(safe_list)

    return safe_count


def check_dir_and_diff(a, b, prev_dir):

    cur_dir = 1 if a > b else -1
    same_dir = cur_dir == prev_dir

    in_range = 0 < abs(a - b) <= 3
    return same_dir and in_range


# Future Me: Options from other solutions
# ---------------------------------------
# zip[list, list[1:]] creates a list of numbers and same list offset
# Then diff between each pair:
#   d > 0 for d in new_list
#   1 <= abs(diff) <= 3
# python all command to check all are true  (not any)
# checks all the same direction and in range


def check_report(rep):

    a = rep[0]
    prev_dir = None

    for n in range(1, len(rep)):
        b = rep[n]
        curr_dir = 1 if a > b else -1

        if prev_dir is None:
            prev_dir = curr_dir

        if check_dir_and_diff(a, b, prev_dir):
            a = b
            prev_dir = curr_dir
            continue

        # Means not safe so can return
        return False

    return True


def part2(data):
    """Solve part 2"""

    safe_list = []
    safe_count = 0
    pos = 0

    while pos < len(data):
        still_safe = True
        fail_safe = True

        report = data.pop(0)
        a = report[0]
        prev_dir = None

        print("\n", report)

        for n in range(1, len(report)):
            b = report[n]
            curr_dir = 1 if a > b else -1

            if prev_dir is None:
                prev_dir = curr_dir

            check_pair = check_dir_and_diff(a, b, prev_dir)
            print(n, ":", "a", a, "b", b, a - b, prev_dir, curr_dir, check_pair)

            if check_pair:
                a = b
                prev_dir = curr_dir
                continue

            print("Difference unsafe")
            still_safe = False
            break

        if not still_safe:
            for i in range(len(report)):
                new_report = report[:i] + report[i + 1 :]
                if check_report(new_report):
                    print("new ok", new_report)
                    still_safe = True
                    break

        if still_safe:
            safe_list.append(report)
            safe_count += 1

    print(safe_list)

    return safe_count


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
    tests = solve(test_file2, run="Test2")

    print()
    solutions = solve(soln_file)
