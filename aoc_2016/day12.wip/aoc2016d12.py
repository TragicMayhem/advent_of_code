# https://adventofcode.com/2016/day/12

import pathlib
import time

script_path = pathlib.Path(__file__).parent
soln_file = script_path / "input.txt"  # 317993 (1s) / 9227647  (28s)
test_file = script_path / "test.txt"  #  42         / 42


def parse(puzzle_input):
    """Parse input"""

    with open(puzzle_input, "r") as file:
        data = file.read().split("\n")
        instr = []

        for x in data:
            instr.append(tuple(x.split()))

    return instr


def get_val(v, reg):
    try:
        return int(v)
    except:
        return reg[v]


def process_instructions(data, c=0):
    registers = {"a": 0, "b": 0, "c": c, "d": 0}

    print(data)

    point = 0

    while point <= len(data) - 1:
        next = data[point]

        if next[0] == "jnz":
            if get_val(next[1], registers) != 0:
                point += int(next[2])
                continue

        elif next[0] == "cpy":
            registers[next[2]] = get_val(next[1], registers)

        elif next[0] == "inc":
            registers[next[1]] += 1

        elif next[0] == "dec":
            registers[next[1]] -= 1

        point += 1

    return registers["a"]


def solve(puzzle_input):
    """Solve the puzzle for the given input"""
    times = []

    data = parse(puzzle_input)

    times.append(time.perf_counter())
    solution1 = process_instructions(data)
    times.append(time.perf_counter())
    solution2 = process_instructions(data, c=1)
    times.append(time.perf_counter())

    return solution1, solution2, times


def runTest(test_file):
    data = parse(test_file)
    test_solution1 = process_instructions(data)
    test_solution2 = process_instructions(data, c=1)
    return test_solution1, test_solution2


def runAllTests():
    print("Tests")
    a, b = runTest(test_file)
    print(f"Test1.  Part1: {a} Part 2: {b}")


if __name__ == "__main__":  # print()
    runAllTests()

    solutions = solve(soln_file)
    print("\nAOC")
    print(f"Solution 1: {str(solutions[0])} in {solutions[2][1]-solutions[2][0]:.4f}s")
    print(f"Solution 2: {str(solutions[1])} in {solutions[2][2]-solutions[2][1]:.4f}s")
    print(f"\nExecution total: {solutions[2][-1]-solutions[2][0]:.4f} seconds")
