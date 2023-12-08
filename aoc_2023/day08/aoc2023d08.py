# https://adventofcode.com/2023/day/8

import pathlib
import time
from itertools import cycle, product
from math import lcm

script_path = pathlib.Path(__file__).parent
input = script_path / "input.txt"  # 13301 / 7309459565207
input_test = script_path / "test.txt"  # 6 /
input_test_pt2 = script_path / "test_pt2.txt"  # 6 /

# itertool cycle
# https://docs.python.org/3/library/itertools.html
# https://www.geeksforgeeks.org/python-itertools-cycle/
#  # cycle('ABCD') --> A B C D A B C D A B C D ...

# itertools product
# https://docs.python.org/3/library/itertools.html#itertools.product
# product('ABCD', 'xy') --> Ax Ay Bx By Cx Cy Dx Dy
# https://note.nkmk.me/en/python-itertools-product/

# Hints from Slack at work
# Prime numbers, lowest common multiple
#    Some functions people have written but someone posted math has lcm
#    math.lcm(*repeatingLengths)


def parse(puzzle_input):
    """Parse input"""

    routes = {}

    with open(puzzle_input, "r") as file:
        #  Read each line (split \n) and form a list of strings
        lst = file.read().split("\n\n")

        directions = lst.pop(0)

        lst = lst[0].split("\n")
        lst = [l.split(" = ") for l in lst]

        for l in lst:
            start = l[0]
            left, right = l[1][1:-1].replace(" ", "").split(",")

            routes[start] = (left, right)
        # print(routes)

    return (directions, routes)


def part1(data):
    """Solve part 1"""

    directions, map = data

    # print(directions)
    # print(map)

    steps = 1

    start = "AAA"
    target = "ZZZ"

    current = start
    for next_move in cycle(directions):
        if next_move == "L":
            current = map[current][0]
        else:
            current = map[current][1]

        # print(current)

        if current == target:
            break

        steps += 1

    return steps


def part2(data):
    """Solve part 2"""

    directions, map = data

    possible_starts = []
    possible_ends = []

    possible_steps = []

    # Create a list of places the ghosts can start and where they can end based on the last char
    for parent, child in map.items():
        # print(parent, child)

        if parent[-1] == "A":
            # Doh, I was adding a child here and it doesnt work surprisngly
            possible_starts.append(parent)

        if child[0][-1] == "Z":
            possible_ends.append(child[0])
        if child[1][-1] == "Z":
            possible_ends.append(child[1])

    print(possible_starts)
    print(possible_ends)

    #

    # Reading more hints after realising brute force will take long tim
    # Any of the starts could end up at any of the ends. We dont know what.
    # So need to work out all the combinations - thats where itertools.product comes in

    # Copy part 1 and run another loop around it but only look for ending in Z exits

    for start, _ in product(possible_starts, possible_ends):
        steps = 1
        current = start

        for next_move in cycle(directions):
            if next_move == "L":
                current = map[current][0]
            else:
                current = map[current][1]

            if current[-1] == "Z":
                break

            steps += 1

        possible_steps.append(steps)

    print(possible_steps)

    ans = lcm(*possible_steps)

    return ans


def solve(puzzle_input, run="Solution"):
    """Solve the puzzle for the given input"""
    times = []

    print("\n", run)
    pt1, pt2 = False, False
    if run == "Solution":
        pt1 = True
        pt2 = True
    elif run[-3:] == "Pt1":
        pt1 = True
    elif run[-3:] == "Pt2":
        pt2 = True

    data = parse(puzzle_input)

    times.append(time.perf_counter())

    solution1 = part1(data) if pt1 else None

    times.append(time.perf_counter())

    solution2 = part2(data) if pt2 else None

    times.append(time.perf_counter())

    print(f"{run} 1: {str(solution1)} in {times[1]-times[0]:.4f}s")
    print(f"{run} 2: {str(solution2)} in {times[2]-times[1]:.4f}s")
    print(f"\nExecution total: {times[-1]-times[0]:.4f} seconds")

    return solution1, solution2, times


if __name__ == "__main__":
    print("\nAOC")

    tests = solve(input_test, run="Test Pt1")
    tests_pt2 = solve(input_test_pt2, run="Test Pt2")

    print()
    solutions = solve(input)
