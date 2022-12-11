# https://adventofcode.com/2022/day/11

import pathlib
import time
from collections import defaultdict
from pprint import pprint as pp
from copy import deepcopy

## Added to use in math of part 2 to reduce calculations
from math import floor, lcm, gcd

## Add deque and had to change over part 1 also - needed to solve part 2 its quicker
from collections import deque

script_path = pathlib.Path(__file__).parent
input = script_path / "input.txt"  # 112815  // 25738411485
input_test = script_path / "test.txt"  # 10605 // 2713310158

# TO DO - How to use objects?  Must be better option.


def parse(puzzle_input):
    """Parse input"""

    with open(puzzle_input, "r") as file:
        lst = file.read().split("\n\n")

    monkeys = defaultdict(dict)

    for m in lst:
        lines = m.split("\n")
        id = int(lines[0][7:-1])
        monkeys[id] = defaultdict(dict)

        items = deque(map(int, lines[1].split(":")[1].split(", ")))
        monkeys[id]["items"] = items

        inst = lines[2].split("old ")[1].split(" ")
        monkeys[id]["op"] = inst[0]
        monkeys[id]["op_val"] = inst[1]

        monkeys[id]["div_by"] = int(lines[3].split("by ")[1])
        monkeys[id]["true"] = int(lines[4].split("monkey ")[1])
        monkeys[id]["false"] = int(lines[5].split("monkey ")[1])
        monkeys[id]["count"] = 0

    return monkeys


def part1(data):
    """Solve part 1"""

    rounds = 20
    monkeys = deepcopy(data)
    num_monkeys = len(monkeys.keys())
    for r in range(rounds):

        for m in range(num_monkeys):

            if len(monkeys[m].get("items", deque())) == 0:
                continue
            else:
                monkey_queue = monkeys[m].get("items", deque())

            next_item = monkey_queue.popleft()

            while next_item:
                monkeys[m]["count"] += 1

                if monkeys[m].get("op_val") == "old":
                    val = next_item
                else:
                    val = int(monkeys[m].get("op_val"))

                if monkeys[m].get("op") == "*":
                    calc_worry = floor((next_item * val) / 3)
                else:
                    calc_worry = floor((next_item + val) / 3)

                decide = calc_worry % monkeys[m].get("div_by")

                if decide == 0:
                    to_monkey = monkeys[m].get("true")
                else:
                    to_monkey = monkeys[m].get("false")

                monkeys[to_monkey].get("items", deque).append(calc_worry)

                if monkey_queue:
                    next_item = monkey_queue.popleft()
                else:
                    next_item = None
                    monkeys[m]["items"] = deque()

    pp(monkeys)
    item_counts = []
    for m in monkeys:
        item_counts.append(monkeys[m]["count"])

    item_counts.sort(reverse=True)
    print(item_counts)
    ans = item_counts[0] * item_counts[1]

    return ans


def part2(data):
    """Solve part 2"""

    rounds = 10000
    monkeys = deepcopy(data)
    num_monkeys = len(monkeys.keys())

    # the numbers and calculations get to big, the operations slow down about round 800 and doesnt run
    # I tried a few paper based math ideas, and then looked for some hints before realising math had lcm to make this easier
    # The items and worries are not important, just the number at the end to see where the worry goes to - True or False
    # the lcm reduces the calculation down for all items with a constant factor based on all the div_by values
    # the modulus then allows small number process across all items correctly as only worried about the end decision and passing item

    dividers_list = []
    for m in monkeys:
        dividers_list.append(monkeys[m]["div_by"])
    pt2_modulus = lcm(*dividers_list)
    print(dividers_list)

    for r in range(rounds):
        print(r)
        for m in range(num_monkeys):

            if len(monkeys[m].get("items", deque())) == 0:
                continue
            else:
                monkey_queue = monkeys[m].get("items", deque())

            monkeys[m]["count"] += len(monkey_queue)
            next_item = monkey_queue.popleft()

            while next_item:

                if monkeys[m].get("op_val") == "old":
                    val = next_item
                else:
                    val = int(monkeys[m].get("op_val"))

                if monkeys[m].get("op") == "*":
                    calc_worry = next_item * val
                else:
                    calc_worry = next_item + val

                calc_worry = calc_worry % pt2_modulus
                decide = calc_worry % monkeys[m].get("div_by")

                if decide == 0:
                    to_monkey = monkeys[m].get("true")
                else:
                    to_monkey = monkeys[m].get("false")

                monkeys[to_monkey].get("items", deque).append(calc_worry)

                if monkey_queue:
                    next_item = monkey_queue.popleft()
                else:
                    next_item = None
                    monkeys[m]["items"] = deque()

    pp(monkeys)
    item_counts = []
    for m in monkeys:
        item_counts.append(monkeys[m]["count"])

    item_counts.sort(reverse=True)
    print(item_counts)
    ans = item_counts[0] * item_counts[1]

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
