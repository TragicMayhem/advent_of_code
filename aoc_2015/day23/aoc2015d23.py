# https://adventofcode.com/2015/day/23

import pathlib
import time

script_path = pathlib.Path(__file__).parent
soln_file = script_path / "input.txt"  # a=1 b=307 / a=1 b=160
test_file = script_path / "test.txt"  # a=2, b=0 / a=7 b=0

# Two registers starting values for processing part 1 and part 2
part1 = [0, 0]  # a=1 b=307
part2 = [1, 0]  # a=1 b=160


def parse(puzzle_input):
    """Parse input"""
    with open(puzzle_input, "r") as file:
        lst = file.read().split("\n")  # Read file make list bu splitting on new line \n
        data = []
        for x in lst:
            if x.find(",") > 0:
                line = x.split()
                data.append((line[0], line[1][:-1], int(line[2])))
            else:
                line = x.split()
                try:
                    val = int(line[1])
                except:
                    val = line[1]
                data.append((line[0], val))

    return data


def process_instructions(start, data):
    pointer = 0
    registers = start

    while pointer < len(data):
        d = data[pointer]
        reg_to_change = 0 if d[1] == "a" else 1
        # print("Current pointer:", pointer,"d:" , d, "reg idx:" ,reg_to_change)

        if d[0] == "jie":  # 3 element tuple
            if registers[reg_to_change] % 2 == 0:
                pointer += d[2]
            else:
                pointer += 1

        elif d[0] == "jio":  # 3 element tuple
            if registers[reg_to_change] == 1:
                pointer += d[2]
            else:
                pointer += 1

        elif d[0] == "inc":
            registers[reg_to_change] += 1
            pointer += 1

        elif d[0] == "tpl":
            registers[reg_to_change] *= 3
            pointer += 1

        elif d[0] == "hlf":
            registers[reg_to_change] //= 2
            pointer += 1

        elif d[0] == "jmp":
            pointer += d[1]

    return registers


def solve(puzzle_input):
    """Solve the puzzle for the given input"""
    times = []

    data = parse(puzzle_input)
    times.append(time.perf_counter())

    solution1 = process_instructions(part1[:], data)
    times.append(time.perf_counter())

    solution2 = process_instructions(part2[:], data)
    times.append(time.perf_counter())

    return solution1, solution2, times


def runAllTests():
    print("\nTests\n")
    a, b, t = solve(test_file)
    print(f"Test1 Part 1: {a} in {t[1]-t[0]:.4f}s")
    print(f"      Part 2: {b} in {t[2]-t[1]:.4f}s")
    print(f"      Execution total: {t[-1]-t[0]:.4f} seconds")


if __name__ == "__main__":  # print()
    runAllTests()

    sol1, sol2, times = solve(soln_file)
    print("\nAOC")
    print(f"Solution 1: {str(sol1)} in {times[1]-times[0]:.4f}s")
    print(f"Solution 2: {str(sol2)} in {times[2]-times[1]:.4f}s")
    print(f"\nExecution total: {times[-1]-times[0]:.4f} seconds")
