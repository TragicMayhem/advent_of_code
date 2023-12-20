# https://adventofcode.com/2015/day/4

import time
import hashlib

# Takes AGES to run :D

soln_file = "yzbqklnj"  # 282749 / 9962624
test_file = "abcdef"  # 609043 = 000001dbbfa...   / 6742839
test_file2 = "pqrstuv"  #  1048970 = 000006136ef....  / 5714438


def part1(key):
    """Solve part 1"""

    i = 0

    while True:
        current = key + str(i)
        current_hash = hashlib.md5(current.encode()).hexdigest()
        if current_hash.startswith("00000"):
            break
        i += 1

    # print(f"The solution is {i} MD5 of {current} is {current_hash}")

    return i


def part2(key):
    """Solve part 2"""
    i = 0

    while True:
        current = key + str(i)
        current_hash = hashlib.md5(current.encode()).hexdigest()
        if current_hash.startswith("000000"):
            break
        i += 1

    # print(f"The solution is {i} MD5 of {current} is {current_hash}")
    return i


def solve(puzzle_input):
    """Solve the puzzle for the given input"""
    times = []
    times.append(time.perf_counter())
    solution1 = part1(puzzle_input)
    times.append(time.perf_counter())
    solution2 = part2(puzzle_input)
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
    print("....takes a while to run......")

    runAllTests()

    sol1, sol2, times = solve(soln_file)
    print("\nAOC")
    print(f"Solution 1: {str(sol1)} in {times[1]-times[0]:.4f}s")
    print(f"Solution 2: {str(sol2)} in {times[2]-times[1]:.4f}s")
    print(f"\nExecution total: {times[-1]-times[0]:.4f} seconds")
