# https://adventofcode.com/2022/day/21

import pathlib
import time
from collections import defaultdict, deque

script_path = pathlib.Path(__file__).parent
input = script_path / "input.txt"  # 268597611536314 /
input_test = script_path / "test.txt"  # 152

monkeys = defaultdict(list)
monkey_nums = defaultdict(list)


def parse(puzzle_input):
    """Parse input"""

    monkeys.clear()
    monkey_nums.clear()

    with open(puzzle_input, "r") as file:
        details = file.read().split("\n")

    for d in details:
        mky, ans = d.split(": ")
        monkeys[mky] = ans
        if ans.isdigit():
            monkey_nums[mky] = int(ans)

    # print("monkeys", len(monkeys), "monkey_nums", len(monkey_nums))
    return None


def compute_monkey_value(mky):
    # print("mky", mky)
    if mky in monkey_nums:
        # print("rtn", monkey_nums[mky])
        return monkey_nums[mky]

    val = monkeys[mky]
    l, op, r = val.split()
    # print(l,":",op,":",r)

    l_val = compute_monkey_value(l)
    r_val = compute_monkey_value(r)

    if op == "+":
        ans = l_val + r_val
    elif op == "-":
        ans = l_val - r_val
    elif op == "*":
        ans = l_val * r_val
    elif op == "/":
        ans = int(l_val / r_val)

    # print(ans)
    monkey_nums[mky] = ans

    return ans


def part1():
    """Solve part 1"""

    ans = compute_monkey_value("root")

    return ans


def part2():
    """Solve part 2"""

    return 2


def solve(puzzle_input):
    """Solve the puzzle for the given input"""
    times = []

    parse(puzzle_input)

    times.append(time.perf_counter())
    solution1 = part1()
    times.append(time.perf_counter())
    solution2 = part2()
    times.append(time.perf_counter())

    return solution1, solution2, times


def runTest(test_file):

    parse(test_file)
    # Test data check for function
    print("lfqf", compute_monkey_value("lfqf"))
    print("drzm", compute_monkey_value("drzm"))
    print("sjmn", compute_monkey_value("sjmn"))
    print("pppw", compute_monkey_value("pppw"))
    print()

    test_solution1 = part1()
    test_solution2 = part2()
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
