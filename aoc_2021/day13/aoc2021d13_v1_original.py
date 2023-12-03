# https://adventofcode.com/2021/day/13

import pathlib
import time
from types import CoroutineType

script_path = pathlib.Path(__file__).parent
input = script_path / "input.txt"  # 655 /
input_test = script_path / "test.txt"  # 17 /


def parse(puzzle_input):
    """Parse input"""
    data = set()  # not list, to deal with unique values where dots overlap
    folds = []

    with open(puzzle_input, "r") as file:
        lines = [d.split(",") for d in file.read().split("\n")]

        for l in lines:
            if l[0] == "":
                continue

            if "=" in l[0]:
                folds.append(l[0][l[0].index("=") - 1 :].split("="))
                continue
            data.add((int(l[0]), int(l[1])))

        # print(folds)
        # print(data)

    return data, folds


def isVertical(axis):
    return True if axis == "x" else False


def foldSheet(grid, axis, foldLine):
    # print("Folding:",axis,foldLine)
    verticalFold = isVertical(axis)
    newGrid = set()

    for x, y in grid:
        # print(x,y)

        if verticalFold:
            if x > foldLine:
                x = foldLine - (x - foldLine)
        else:
            if y > foldLine:
                y = foldLine - (y - foldLine)

        newGrid.add((x, y))

    return newGrid


def part1(d, f):
    """Solve part 1"""

    # print(d, f)

    fold = f[0][0]
    line = int(f[0][1])
    new = foldSheet(d, fold, line)

    return len(new)


def showGrid(d):
    print()
    grid = list(d)

    size_x = -1
    size_y = -1

    for x, y in d:
        if x > size_x:
            size_x = x
        if y > size_y:
            size_y = y

    print("Grid", size_x, "by", size_y)

    display = []
    for y in range(size_y + 1):
        line = ""
        for x in range(size_x + 1):
            line += "#" if (x, y) in d else " "
        display.append(line)

    for line in display:
        print(line)


def part2(d, f):
    """Solve part 2"""

    for nextFold_axis, nextFold_line in f:
        print("Folding", nextFold_axis, nextFold_line)
        d = foldSheet(d, nextFold_axis, int(nextFold_line))
        # print(d)

    showGrid(d)

    return 1


def solve(puzzle_input, run="Solution"):
    """Solve the puzzle for the given input"""
    times = []

    data, folds = parse(puzzle_input)

    times.append(time.perf_counter())
    solution1 = part1(data, folds)
    times.append(time.perf_counter())
    solution2 = part2(data, folds)
    times.append(time.perf_counter())

    print(f"{run} 1: {str(solution1)} in {times[1]-times[0]:.4f}s")
    print(f"{run} 2: {str(solution2)} in {times[2]-times[1]:.4f}s")
    print(f"\nExecution total: {times[-1]-times[0]:.4f} seconds")

    return solution1, solution2, times


if __name__ == "__main__":
    print("\nAOC")

    tests = solve(input_test, run="Test")

    print()
    solutions = solve(input)
