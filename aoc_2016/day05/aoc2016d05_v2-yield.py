# https://adventofcode.com/2016/day/5

import pathlib
import time
import hashlib

script_path = pathlib.Path(__file__).parent
input = script_path / "input.txt"  # f97c354d  (10s)   / 863dde27  (16s)
input_test = script_path / "test.txt"  # 18f47a30  (8s)    / 05ace8e3  (29s)


def parse(puzzle_input):
    """Parse input"""
    with open(puzzle_input, "r") as file:
        data = file.read().split("\n")
    return data


def yield_hashes(key):
    i = 0

    while True:
        current = key + str(i)
        current_hash = hashlib.md5(current.encode()).hexdigest()
        if current_hash.startswith("00000"):
            # print('yielding', current_hash)
            yield current_hash

        i += 1


def part1(data):
    """Solve part 1"""
    pwd_chars = []

    for pwd in yield_hashes(data[0]):
        pwd_chars.append(pwd[5])
        if len(pwd_chars) == 8:
            break

    return "".join(pwd_chars)


def part2(data):
    """Solve part 2"""
    final = [None] * 8
    hashes = yield_hashes(data[0])

    while None in final:
        pwd = next(hashes)
        # print(pwd)
        if pwd[5] in "01234567":
            if not final[int(pwd[5])]:
                final[int(pwd[5])] = pwd[6]

    return "".join(final)


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
    a, b, t = solve(input_test)
    print(f"Test1 Part 1: {a} in {t[1]-t[0]:.4f}s")
    print(f"      Part 2: {b} in {t[2]-t[1]:.4f}s")
    print(f"      Execution total: {t[-1]-t[0]:.4f} seconds")


if __name__ == "__main__":  # print()
    print("Hashing all combinations takes a little time.....")

    runAllTests()

    sol1, sol2, times = solve(input)
    print("\nAOC")
    print(f"Solution 1: {str(sol1)} in {times[1]-times[0]:.4f}s")
    print(f"Solution 2: {str(sol2)} in {times[2]-times[1]:.4f}s")
    print(f"\nExecution total: {times[-1]-times[0]:.4f} seconds")
