# https://adventofcode.com/2022/day/21

import pathlib
import time
from collections import defaultdict, deque

script_path = pathlib.Path(__file__).parent
soln_file = script_path / "input.txt"  # 268597611536314 /
test_file = script_path / "test.txt"  # 152

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


def part1(data):
    """Solve part 1"""

    ans = compute_monkey_value("root")

    return ans


def part2(data):
    """Solve part 2"""

    return 2


# def runTest(test_file):
#     parse(test_file)
#     # Test data check for function
#     print("lfqf", compute_monkey_value("lfqf"))
#     print("drzm", compute_monkey_value("drzm"))
#     print("sjmn", compute_monkey_value("sjmn"))
#     print("pppw", compute_monkey_value("pppw"))
#     print()

#     test_solution1 = part1()
#     test_solution2 = part2()
#     return test_solution1, test_solution2


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
