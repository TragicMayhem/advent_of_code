# https://adventofcode.com/2015/day/2

import pathlib
import time

script_path = pathlib.Path(__file__).parent
soln_file = script_path / "input.txt"  # 1588178 / 33783759
test_file = script_path / "test.txt"  # 101 / 48


def parse(puzzle_input):
    """Parse input"""

    with open(puzzle_input, "r") as file:
        lst = file.read().split(
            "\n"
        )  #  Read each line (split \n) and form a list of strings
        lst = [
            x.replace("x", " ").split() for x in lst
        ]  # Split on 'x' in each string ('1x2x3')

        # lst is now a list of lists, sub lists have single characters e.g. [['2', '3', '4'], ['1', '1', '10']]
        # To convert each of the strings to integers you use list comprehension twice anduse [] to put back in list
        converted_list = [[int(dim) for dim in sub_list] for sub_list in lst]

    return converted_list


def part1(data):
    """Solve part 1"""

    total = 0

    for x in data:
        # Each x should be three numbers
        w, l, h = x
        side_areas = [w * l, w * h, h * l]
        total += 2 * sum(side_areas) + min(side_areas)

    # print("Total square foot of paper required is", total)

    return total


def part2(data):
    """Solve part 2"""

    total = 0

    for x in data:
        # Each x should be three numbers
        w, l, h = x
        smallest_perimeter = min(
            [2 * x for x in [l + w, h + l, w + h]]
        )  # Build list of one pair sides, double for each perimter, find min
        volume = w * h * l
        total += smallest_perimeter + volume

    # print("Total ribbon required is", total)

    return total


def solve(puzzle_input):
    """Solve the puzzle for the given input"""
    times = []

    data = parse(puzzle_input)

    times.append(time.perf_counter())
    solution1 = part1(data)
    times.append(time.perf_counter())
    solution2 = part2(data)
    times.append(time.perf_counter())

    return solution1, solution2, times


def runAllTests():
    print("\nTests\n")
    a, b, t = solve(test_file)
    print(f"Test1 Part 1: {a} in {t[1]-t[0]:.4f}s")
    print(f"      Part 2: {b} in {t[2]-t[1]:.4f}s")
    print(f"      Execution total: {t[-1]-t[0]:.4f} seconds")


if __name__ == "__main__":  # print()
    runAllTests()

    sol1, sol2, times = solve(soln_file)
    print("\nAOC")
    print(f"Solution 1: {str(sol1)} in {times[1]-times[0]:.4f}s")
    print(f"Solution 2: {str(sol2)} in {times[2]-times[1]:.4f}s")
    print(f"\nExecution total: {times[-1]-times[0]:.4f} seconds")
