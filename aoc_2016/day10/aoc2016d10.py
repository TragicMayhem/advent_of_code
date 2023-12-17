# https://adventofcode.com/2016/day/10

import pathlib
import time
from collections import defaultdict
from pprint import pprint as pp

script_path = pathlib.Path(__file__).parent
input = script_path / "input.txt"  # 56 /
input_test = script_path / "test.txt"  #


target_values = sorted((61, 17))


def parse(puzzle_input):
    """Parse input"""

    instructions = defaultdict(dict)
    outputs = defaultdict(list)
    values = []

    with open(puzzle_input, "r") as file:
        data = file.read().replace(" to ", " ").split("\n")

        for d in data:
            if d.startswith("value"):
                d = d.replace("value ", "")
                val = int(d[: d.index(" ")])
                target = d[d.index("bot") :]
                values.append((target, val))
            else:
                parts = d.split(" gives ")
                key = parts[0]
                instructions[key] = {"chips": []}

                parts = parts[1].split(" and ")

                first = parts[0][: parts[0].index(" ")]
                first_target = parts[0][len(first) + 1 :]
                instructions[key][first] = first_target

                second = parts[1][: parts[1].index(" ")]
                second_target = parts[1][len(second) + 1 :].strip()
                instructions[key][second] = second_target

                if first_target.startswith("output"):
                    outputs[first_target] = []
                if second_target.startswith("output"):
                    outputs[second_target] = []

        for v in values:
            instructions[v[0]].setdefault("chips", []).append(v[1])

        # print(instructions)
        # print(outputs)

    return (instructions, outputs)


def part1(data):
    """Solve part 1"""

    bots, outputs = data
    bot_target = None

    # print(bots)
    print(outputs)

    queue = list()
    for k, v in bots.items():
        if len(bots[k]["chips"]) == 2:
            queue.append(k)

    print("Initial queue:", queue)

    while queue:
        # print('Queue length:', len(queue), 'with', queue)
        next = queue.pop(0)
        # print('bot has 2 chips:', next, bots[next]['chips'])

        low_target = bots[next]["low"]
        high_target = bots[next]["high"]
        values = sorted(tuple(bots[next]["chips"]))
        # print('low', low_target, '\thigh', high_target, '\tvalues', values)

        if values == target_values:
            print("<<<< Target comparison", next, values, target_values, ">>>>")
            bot_target = next

        # Clear holding bot
        bots[next]["chips"] = []

        if low_target.startswith("out"):
            outputs[low_target].append(values[0])
        else:
            bots[low_target]["chips"].append(values[0])
            if len(bots[low_target]["chips"]) == 2:
                queue.append(low_target)

        if high_target.startswith("out"):
            outputs[high_target].append(values[1])
        else:
            bots[high_target]["chips"].append(values[1])
            if len(bots[high_target]["chips"]) == 2:
                queue.append(high_target)

    # pp(bots)
    print("\nOutput Bins")
    print(outputs)
    answer = outputs["output 0"][0] * outputs["output 1"][0] * outputs["output 2"][0]

    return bot_target, answer


def solve(puzzle_input):
    """Solve the puzzle for the given input"""
    times = []

    data = parse(puzzle_input)
    times.append(time.perf_counter())
    solution1, solution2 = part1(data)
    times.append(time.perf_counter())

    return solution1, solution2, times


def runTest(test_file):
    data = parse(test_file)
    test_solution1, test_solution2 = part1(data)
    return test_solution1, test_solution2


def runAllTests():
    print("Tests")
    a, b = runTest(input_test)
    print(f"Test1.  Part1: {a} Part 2: {b}")


if __name__ == "__main__":  # print()
    runAllTests()

    solutions = solve(input)
    print("\nAOC")
    print(f"Solution 1: {str(solutions[0])}")
    print(f"Solution 2: {str(solutions[1])}")
    print(f"\nExecution total: {solutions[2][-1]-solutions[2][0]:.4f} seconds")
