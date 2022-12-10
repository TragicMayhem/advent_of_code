# https://adventofcode.com/2022/day/10

import pathlib
import time

script_path = pathlib.Path(__file__).parent
input = script_path / "input.txt"  # 12640 // EHBZLRJR
input_test = script_path / "test.txt"  # 13140 //


def parse(puzzle_input):
    """Parse input"""

    with open(puzzle_input, "r") as file:
        lst = file.read().split("\n")

    return lst


def part1(data):
    """Solve part 1"""

    cycle = 1
    x = 1
    strengths = []

    for d in data:
        # print("cycle start: ", d, cycle, x)

        cycle += 1

        if d[:4] == "noop":
            pass
        elif d[:4] == "addx":

            if cycle % 40 == 20:
                # print("key cycle in addx", cycle, x, cycle * x)
                strengths.append(cycle * x)

            cycle += 1
            power = int(d[5:])
            x += power

        if cycle % 40 == 20:
            # print("key cycle", cycle, x, cycle * x)
            strengths.append(cycle * x)

    # print(strengths)

    return sum(strengths)


def get_sprite(cycle, x):
    sprite_position = cycle % 40
    if x <= sprite_position <= x + 2:
        return "#"
    else:
        return " "


def part2(data):
    """Solve part 2"""

    cycle = 1
    x = 1
    line = []
    screen = []

    for d in data:
        # print("cycle start: ", d, cycle, x)
        # Check for sprite before increasing the cycle counter
        # lines are 40 wide, so any remainder is the position
        # sprites are 3 pixles, so check is in a range before and after
        line.append(get_sprite(cycle, x))

        cycle += 1

        if d[:4] == "noop":
            pass

        elif d[:4] == "addx":
            if cycle % 40 == 1:
                # Remainder of 1 means new line, store and reset
                screen.append("".join(line))
                line = []

            line.append(get_sprite(cycle, x))

            cycle += 1
            power = int(d[5:])
            x += power

        if cycle % 40 == 1:
            # Remainder of 1 means new line, store and reset
            screen.append("".join(line))
            line = []

    print("\nMonitor display:")

    for i in screen:
        print(i)

    return True


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

    print("Test 1")
    a, b = runTest(input_test)
    print(f"Test 1.  Part1: {a} Part 2: {b}")


if __name__ == "__main__":

    runAllTests()

    solutions = solve(input)
    print("\nAOC")
    print(f"Solution 1: {str(solutions[0])} in {solutions[2][1]-solutions[2][0]:.4f}s")
    print(f"Solution 2: {str(solutions[1])} in {solutions[2][2]-solutions[2][1]:.4f}s")
    print(f"\nExecution total: {solutions[2][-1]-solutions[2][0]:.4f} seconds")
