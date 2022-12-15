# https://adventofcode.com/2022/day/8

import pathlib
import time
from pprint import pprint as pp
import itertools

script_path = pathlib.Path(__file__).parent
input = script_path / "input.txt"  # 1776 //  234416
input_test = script_path / "test.txt"  # 21  // 8

direction_visiblity = [[]]


def parse(puzzle_input):
    """Parse input"""

    with open(puzzle_input, "r") as file:
        lst = file.read().split("\n")

    trees = [list(n) for n in lst]
    trees = [[int(x) for x in row] for row in trees]

    return trees

def part1(data):
    """Solve part 1"""

    h, w = len(data), len(data[0])
    h_max = h - 1
    w_max = w - 1

    visilbity_count = 0

    for r, row in enumerate(data):
        for c, val in enumerate(row):
            # print(r, c, " height: ", data[r][c])

            # need to check 4 ways and store, then do ANY

            if r == 0 or r == w_max or c == 0 or c == h_max:
                # print("Edge")
                visilbity_count += 1
            else:

                # Replaces my for loops within forloops with list comprehension and
                # then directly use the all

                # Use list splice to get just the data from current tree
                visible_left = all(val > tree for tree in row[c + 1 :])
                visible_right = all(val > tree for tree in row[:c])

                # Have to lock column and go up and down, rather than the getcoords which only generates
                # one cardinal, not loops through use list comprenetion with the right range
                visible_up = all(val > data[rr][c] for rr in range(r + 1, w))
                visible_down = all(val > data[rr][c] for rr in range(r - 1, -1, -1))

                if any([visible_left, visible_right, visible_up, visible_down]):
                    # print("  Tree visible")
                    visilbity_count += 1

    return visilbity_count


def part2(data):
    """Solve part 2"""
    print("Part 2")

    h, w = len(data), len(data[0])
    h_max = h - 1
    w_max = w - 1

    highest_score = 0

    for r, row in enumerate(data):
        # print(r, row)
        if r == 0 or r == w_max:
            continue

        for c, val in enumerate(row):
            if c == 0 or c == h_max:
                continue

            # print("\n", r, c, " height: ", data[r][c])
            count_left = count_right = count_up = count_down = 0

            # Cant work out nce way to list them or yeild with out doing separately
            # so might as well just put for loops here

            for cl in range(c - 1, -1, -1):
                # print("left", r, cl, ": ", data[r][cl])
                if data[r][cl] >= val:
                    # print("left break")
                    break


            for cr in range(c + 1, w, 1):
                # print("right", r, cr, ": ", data[r][cr])
                if data[r][cr] >= val:
                    # print("right break")
                    break


            for cu in range(r - 1, -1, -1):
                # print("up", cu, c, ": ", data[cu][c])
                if data[cu][c] >= val:
                    # print("up break")
                    break


            for cd in range(r + 1, h, 1):
                # print("down", cd, c, ": ", data[cd][c])
                if data[cd][c] >= val:
                    # print("down break")
                    break


            count_left = c - cl
            count_right = cr - c
            count_up = r - cu
            count_down = cd - r
            tree_score = count_left * count_right * count_up * count_down
          
            highest_score = tree_score if tree_score > highest_score else highest_score
            # print(highest_score)

    return highest_score


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


def runTest(test_file):
    data = parse(test_file)
    test_solution1 = part1(data)
    test_solution2 = part2(data)
    return test_solution1, test_solution2


def runAllTests():

    print("Tests")
    a, b = runTest(input_test)
    print(f"Test1.  Part1: {a} Part 2: {b}")


if __name__ == "__main__":

    runAllTests()

    solutions = solve(input)
    print("\nAOC")
    print(f"Solution 1: {str(solutions[0])} in {solutions[2][1]-solutions[2][0]:.4f}s")
    print(f"Solution 2: {str(solutions[1])} in {solutions[2][2]-solutions[2][1]:.4f}s")
    print(f"\nExecution total: {solutions[2][-1]-solutions[2][0]:.4f} seconds")
