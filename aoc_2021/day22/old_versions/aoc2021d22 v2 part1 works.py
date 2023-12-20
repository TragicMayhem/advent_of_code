# https://adventofcode.com/2021/day/x

from os import X_OK
import pathlib
import time
import numpy as np

script_path = pathlib.Path(__file__).parent
soln_file = script_path / "input.txt"  # 583636
test_file = script_path / "test.txt"  # 39
test_file2 = script_path / "test2.txt"  # 590784


def parse(puzzle_input):
    """Parse input"""
    # example: on x=10..10,y=10..10,z=10..10

    instructions = []

    with open(puzzle_input, "r") as file:
        data = file.read().replace(",", " ").split("\n")

        data = [d.split(" ") for d in data]
        # print(data)

        for d in data:
            step = 1 if d[0] == "on" else 0

            first = d[1][2:].split("..")
            second = d[2][2:].split("..")
            third = d[3][2:].split("..")
            # print(step, first, second, third)
            (x1, x2) = map(int, first)
            (y1, y2) = map(int, second)
            (z1, z2) = map(int, third)
            instructions.append(tuple([step, (x1, x2), (y1, y2), (z1, z2)]))

    # print(instructions)
    return instructions


def part1(data, reactor_size):
    """Solve part 1"""
    # example: (1, (10, 12), (10, 12), (10, 12))
    size = reactor_size

    reactor = np.zeros((2 * size, 2 * size, 2 * size))

    for d in data:
        # print(d)
        step = d[0]

        # x,y,z = d[1],d[2],d[3]
        # print(x,y,z)
        # add size to move the coords from neg to pos to use numpy

        # (x1,x2), (y1,y2), (z1,z2) = d[1], d[2], d[3]
        (x1, x2), (y1, y2), (z1, z2) = d[1], d[2], d[3]
        # print(x1,x2, y1,y2, z1,z2)

        if (
            max(abs(x1), abs(x2)) > size
            or max(abs(y1), abs(y2)) > size
            or max(abs(z1), abs(z2)) > size
        ):
            continue

        x1 += size
        x2 += size
        y1 += size
        y2 += size
        z1 += size
        z2 += size

        # plus 1??
        (cx, cy, cz) = (x2 - x1 + 1, y2 - y1 + 1, z2 - z1 + 1)
        # print(cx,cy,cz)

        tmp = np.full((cx, cy, cz), step)
        # print('tmp shape', tmp.shape)
        # print('coords',x1,x2,y1,y2,z1,z2)

        reactor[x1 : x2 + 1, y1 : y2 + 1, z1 : z2 + 1] = tmp

    # print(reactor)
    print(reactor.sum())
    return int(reactor.sum())


def part2(data, reactor_size):
    """Solve part 2"""

    return 1


def solve(puzzle_input, size):
    """Solve the puzzle for the given input"""
    times = []

    data = parse(puzzle_input)

    times.append(time.perf_counter())
    solution1 = part1(data, size)

    times.append(time.perf_counter())
    solution2 = part2(data, size)
    times.append(time.perf_counter())

    return solution1, solution2, times


def runTest(test_file, size):
    data = parse(test_file)
    test_solution1 = part1(data, size)
    test_solution2 = part2(data, size)
    return test_solution1, test_solution2


def runAllTests():
    print("Tests")
    a, b = runTest(test_file, 15)
    print(f"Test1.  Part1: {a} Part 2: {b}")
    a, b = runTest(test_file2, 60)
    print(f"Test2.  Part1: {a} Part 2: {b}")


if __name__ == "__main__":  # print()
    runAllTests()

    solutions = solve(input, 50)
    print("\nAOC")
    print(f"Solution 1: {str(solutions[0])} in {solutions[2][1]-solutions[2][0]:.4f}s")
    print(f"Solution 2: {str(solutions[1])} in {solutions[2][2]-solutions[2][1]:.4f}s")
    print(f"\nExecution total: {solutions[2][-1]-solutions[2][0]:.4f} seconds")
