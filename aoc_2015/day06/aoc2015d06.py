# https://adventofcode.com/2015/day/6

import pathlib
import time
import re

script_path = pathlib.Path(__file__).parent
soln_file = script_path / "input.txt"  # 400,410  (Runs slowly!)/ 15,343,601
test_file = script_path / "test.txt"  # 1,000,000 - 1,000 - 4 = 998,996
test_file2 = (
    script_path / "test2.txt"
)  # 3,001,993 = 1m + 2k - 4 + 1 + 2m - 4 = 3m + 2k -7

# Grid = 0,0 to 999,999
# Input: (turn on|turn off|toggle) x1,y1 through x2,y2

grid = [[0 for j in range(1000)] for i in range(1000)]


def parse(puzzle_input):
    """Parse input"""

    with open(puzzle_input, "r") as file:
        data = file.read().split("\n")
    #   data = [d.split(' | ') for d in file.read().split('\n')]

    return data


def update_lights1(change, st, en):
    counter = 0
    st_x, st_y = map(int, st.split(","))
    en_x, en_y = map(int, en.split(","))

    for a in range(st_x, en_x + 1):
        for b in range(st_y, en_y + 1):
            if change == "turn on":
                grid[a][b] = 1
            elif change == "turn off":
                grid[a][b] = 0
            else:  # change == 'toggle':
                grid[a][b] = (
                    0 if grid[a][b] else 1
                )  ## Alternate way: grid[a][b] = 1 - grid[a][b]
            counter += 1

    return counter


def update_lights2(change, st, en):
    counter = 0
    st_x, st_y = map(int, st.split(","))
    en_x, en_y = map(int, en.split(","))

    for a in range(st_x, en_x + 1):
        for b in range(st_y, en_y + 1):
            if change == "turn on":
                grid[a][b] += 1

            elif change == "turn off":
                grid[a][b] -= 1 if grid[a][b] > 0 else 0

            else:  # change == 'toggle':
                grid[a][b] += 2


def part1(data):
    """Solve part 1"""

    for item in data:
        # Return list (one tuple) of matches [('turn off', '499,499', '500,500')]
        break_item = re.findall(
            r"(\w*|\w* \w*) (\d{1,},\d{1,}) through (\d{1,},\d{1,})", item
        )

        if break_item:
            instr, coord_start, coord_end = break_item[0]
            # print(instr, coord_start, coord_end)
            update_lights1(instr, coord_start, coord_end)

    lights_on = 0

    for i in range(len(grid)):
        lights_on += grid[i].count(1)
        # print(i, grid[i].count(1))

    # print("Lights on = ", lights_on)
    return lights_on


def part2(data):
    """Solve part 2"""

    for item in data:
        # Return list (one tuple) of matches [('turn off', '499,499', '500,500')]
        break_item = re.findall(
            r"(\w*|\w* \w*) (\d{1,},\d{1,}) through (\d{1,},\d{1,})", item
        )

        if break_item:
            instr, coord_start, coord_end = break_item[0]
            # print(instr, coord_start, coord_end)
            update_lights2(instr, coord_start, coord_end)

    lights_brightness = 0

    for i in range(len(grid)):
        for j in range(len(grid[0])):
            lights_brightness += grid[i][j]

    # print("Lights brightness = ", lights_brightness)

    return lights_brightness


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
