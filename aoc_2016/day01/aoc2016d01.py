# https://adventofcode.com/2016/day/1

# Not the cleanest code to work out, was brain>code and inconsistent testing
# todo probably should tidy up

import pathlib
import time

script_path = pathlib.Path(__file__).parent
soln_file = script_path / "input.txt"  # 236 / 182
test_file = script_path / "test.txt"  # 12 / None
test_file2 = script_path / "test2.txt"  # None / 4


directions = ["N", "E", "S", "W"]


def parse(puzzle_input):
    """Parse input"""
    with open(puzzle_input, "r") as file:
        data = file.read().split(", ")

    return data


def part1(data):
    """Solve part 1"""

    val_ns = val_ew = 0
    facing_ind = 0

    for i in data:
        move_val = int(i[1:])

        if i[0] == "R":
            facing_ind = (facing_ind + 1) if facing_ind < 3 else 0

        if i[0] == "L":
            facing_ind = (facing_ind - 1) if facing_ind > 0 else 3

        if directions[facing_ind] == "N":
            val_ns += move_val
        if directions[facing_ind] == "S":
            val_ns -= move_val
        if directions[facing_ind] == "E":
            val_ew += move_val
        if directions[facing_ind] == "W":
            val_ew -= move_val

    val_ew = val_ew * -1 if val_ew < 0 else val_ew
    val_ns = val_ns * -1 if val_ns < 0 else val_ns

    # print(f'P1 N-S difference: {val_ns} and E-W difference: {val_ew} so distance is {val_ns + val_ew}\n')

    return val_ns + val_ew


def part2(data):
    """Solve part 2"""

    val_ns = val_ew = 0
    pos_ns = pos_ew = 0
    facing_ind = 0
    facing = directions[facing_ind]

    loc = (pos_ns, pos_ew)
    visited_locations = [loc]

    for i in data:
        move_val = int(i[1:])

        if i[0] == "R":
            facing_ind = (facing_ind + 1) if facing_ind < 3 else 0
        elif i[0] == "L":
            facing_ind = (facing_ind - 1) if facing_ind > 0 else 3

        dir = directions[facing_ind]
        pos_ns, pos_ew = loc
        new_loc = None
        visted_already = False

        for p in range(move_val):
            if dir == "N":
                pos_ns += 1
            if dir == "S":
                pos_ns -= 1
            if dir == "E":
                pos_ew += 1
            if dir == "W":
                pos_ew -= 1

            # print(f'{(pos_ns, pos_ew)}')
            new_loc = (pos_ns, pos_ew)

            loc = new_loc

            if new_loc in visited_locations:
                # print(f"Location already visited {new_loc}")
                visted_already = True
                break

            visited_locations.append(new_loc)

        if visted_already:
            break

        # print(visited_locations)
        # print(f'END {i}; {facing_ind}; {directions[facing_ind]} > {loc}\n')

    val_ew = loc[1] * -1 if loc[1] < 0 else loc[1]
    val_ns = loc[0] * -1 if loc[0] < 0 else loc[0]

    # print(f'P2 N-S difference: {val_ns} and E-W difference: {val_ew} so distance is {val_ns + val_ew}\n')

    return val_ns + val_ew


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
