# https://adventofcode.com/2021/day/9

import pathlib
import time

script_path = pathlib.Path(__file__).parent
input = script_path / "input.txt"  # 550
input_test = script_path / "test.txt"  # 15 /

file_in = input_test

grid_size_rows = 0
grid_size_cols = 0


def parse(puzzle_input):
    """Parse input - each line of 10 number signals then 4-digit number"""

    with open(puzzle_input, "r") as file:
        data = [list(d) for d in file.read().split("\n")]

    return data


def check_lowest_height(r, c, grid):
    """ """

    return False


def part1(data):
    """Solve part 1"""

    risk = []
    grid = data[:]
    grid_size_rows = len(grid)
    grid_size_cols = len(grid[0])

    print(grid_size_cols, grid_size_rows, grid)

    for r in range(grid_size_rows):
        for c in range(grid_size_cols):
            value = grid[r][c]
            # print("main",r,c, "value",value,"max", grid_size_rows,grid_size_cols)

            xposstart = 0 if r == 0 else r - 1
            yposstart = 0 if c == 0 else c - 1
            xposend = grid_size_rows if r + 2 > grid_size_rows else r + 2
            yposend = grid_size_cols if c + 2 > grid_size_cols else c + 2

            # print(xposstart,xposend,yposstart,yposend)
            tally = 0
            count = 0
            for x in range(xposstart, xposend):
                for y in range(yposstart, yposend):
                    # print(x,y,"value", value, "grid[x][y]",grid[x][y])
                    count += 1
                    if (x, y) == (r, c):
                        continue
                    else:
                        if int(value) < int(grid[x][y]):
                            tally += 1

            # print("tally", r,c,":", tally)

            if tally == count - 1:
                risk.append(int(value) + 1)

        # print(risk)
        # print(sum(risk))

    return sum(risk)


def part2(data):
    """Solve part 2"""

    """
    pop the values until 9 and add up
    if edge is not 9 tne start 0 else read untl first non-9 = start
    read along row for non 9 values = stop value
 
    grid[r].pop(0)

    """

    return 1


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

    tests = solve(input_test, run="Test")

    print()
    solutions = solve(input)
