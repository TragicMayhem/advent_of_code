# https://adventofcode.com/2015/day/3

import pathlib
import time

script_path = pathlib.Path(__file__).parent
soln_file = script_path / "input.txt"  # 2592 / 2360
test_file = script_path / "test.txt"  # 2 / 11
test_file2 = script_path / "test2.txt"  # 4 / 3


def parse(puzzle_input):
    """Parse input"""

    with open(puzzle_input, "r") as file:
        directions = list(file.read())

    return directions


def part1(data):
    """Solve part 1"""

    x_pos = y_pos = 0
    locations = {"0,0": 1}

    for dir in data:
        if dir == "^":
            y_pos += 1
        if dir == "v":
            y_pos -= 1
        if dir == "<":
            x_pos -= 1
        if dir == ">":
            x_pos += 1

        loc = str(x_pos) + "," + str(y_pos)
        locations[loc] = locations.get(loc, 0) + 1

    # print(f'\nTotal houses visited at least once = {len(locations)}\n')

    return len(locations)


def part2(data):
    """Solve part 2"""
    santa_x = santa_y = robo_x = robo_y = 0
    locations = {"0,0": 1}
    santas_move = True

    for dir in data:
        if santas_move:
            pos = [santa_x, santa_y]
        else:
            pos = [robo_x, robo_y]

        if dir == "^":
            pos[1] += 1
        if dir == "v":
            pos[1] -= 1
        if dir == "<":
            pos[0] -= 1
        if dir == ">":
            pos[0] += 1

        loc = str(pos[0]) + "," + str(pos[1])
        locations[loc] = locations.get(loc, 0) + 1

        if santas_move:
            santa_x = pos[0]
            santa_y = pos[1]
        else:
            robo_x = pos[0]
            robo_y = pos[1]

        santas_move = not santas_move

    # print(f'\nTotal houses visited at least once = {len(locations)}\n')

    return len(locations)


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


def runAllTests():
    print("\nTests\n")

    a, b, t = solve(test_file)
    print(f"Test1 Part 1: {a} in {t[1]-t[0]:.4f}s")
    print(f"      Part 2: {b} in {t[2]-t[1]:.4f}s")
    print(f"      Execution total: {t[-1]-t[0]:.4f} seconds")

    a, b, t = solve(test_file2)
    print(f"Test2 Part 1: {a} in {t[1]-t[0]:.4f}s")
    print(f"      Part 2: {b} in {t[2]-t[1]:.4f}s")
    print(f"      Execution total: {t[-1]-t[0]:.4f} seconds")


if __name__ == "__main__":  # print()
    runAllTests()

    sol1, sol2, times = solve(soln_file)
    print("\nAOC")
    print(f"Solution 1: {str(sol1)} in {times[1]-times[0]:.4f}s")
    print(f"Solution 2: {str(sol2)} in {times[2]-times[1]:.4f}s")
    print(f"\nExecution total: {times[-1]-times[0]:.4f} seconds")
