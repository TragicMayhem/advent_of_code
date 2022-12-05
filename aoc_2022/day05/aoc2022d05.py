# https://adventofcode.com/2022/day/5

import pathlib
import time
from copy import deepcopy

script_path = pathlib.Path(__file__).parent
input = script_path / "input.txt"  # WSFTMRHPP  //  GSLCMFBRP
input_test = script_path / "test.txt"  # CMZ //  MCD


def parse(puzzle_input):
    """Parse input"""

    with open(puzzle_input, "r") as file:
        parts = file.read().split("\n\n")

    positions = parts[0].split("\n")

    transposed_tuples = list(zip(*positions))
    transposed_tuples = [d[::-1] for d in transposed_tuples]
    transposed_tuples = list(filter(lambda c: c[0] != " ", transposed_tuples))
    transposed_tuples = [[x for x in col if x != " "] for col in transposed_tuples]
    stacks = [x[1:] for x in transposed_tuples]

    instructions_input = parts[1].split("\n")
    instructions_input = [x.split(" ") for x in instructions_input]
    instructions = []
    for el in instructions_input:
        tmp = []
        for x in el:
            try:
                tmp.append(int(x))
            except ValueError:
                pass
        instructions.append(tmp)
    # print(stacks)
    # print(instructions)

    # [['Z', 'N'], ['M', 'C', 'D'], ['P']]
    # [[1, 2, 1], [3, 1, 3], [2, 2, 1], [1, 1, 2]]

    return (stacks, instructions)


def part1(data):
    """Solve part 1"""

    stacks = deepcopy(data[0])
    instructions = deepcopy(data[1])

    for move in instructions:
        how_many, source, target = move
        for i in range(how_many):
            # crate = stacks[source - 1].pop(-1)
            # stacks[target - 1].append(crate)
            stacks[target - 1].append(stacks[source - 1].pop(-1))

    top_crates = [x[-1] for x in stacks]
    ans = "".join(top_crates)

    return ans


def part2(data):
    """Solve part 2"""
    stacks = deepcopy(data[0])
    instructions = deepcopy(data[1])

    for move in instructions:
        how_many, source, target = move
        crates = stacks[source - 1][-how_many:]
        stacks[source - 1] = stacks[source - 1][: len(stacks[source - 1]) - how_many]
        stacks[target - 1].extend(crates)
        # print(stacks)

    top_crates = [x[-1] for x in stacks if len(x) > 0]
    ans = "".join(top_crates)

    return ans


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
