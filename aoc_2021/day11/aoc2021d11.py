# https://adventofcode.com/2021/day/11

import pathlib
import time

# from collections import deque

script_path = pathlib.Path(__file__).parent
soln_file = script_path / "input.txt"  # 1673 (100 steps) /
test_file = script_path / "test.txt"  # 1656 (100 steps)
test_file2 = script_path / "test2.txt"  #

steps = 100


def get_coords_cardinals(r, c, h, w):
    for delta_r, delta_c in ((-1, 0), (1, 0), (0, -1), (0, 1)):
        rr, cc = (r + delta_r, c + delta_c)
        if 0 <= rr < h and 0 <= cc < w:
            yield (rr, cc)


def get_coords_around_all(r, c, h, w):
    for delta_r, delta_c in (
        (-1, 0),
        (1, 0),
        (0, -1),
        (0, 1),
        (-1, -1),
        (-1, 1),
        (1, -1),
        (1, 1),
    ):
        rr, cc = (r + delta_r, c + delta_c)
        if 0 <= rr < h and 0 <= cc < w:
            yield (rr, cc)


# Tried recursion and counting and cant understand! Come back to it?
# def flash_cascade(grid, r, c, h, w, flashed = None):
#     '''
#         This is called when the value at (r,c) is a 9 (flash)
#         So need to add +1 to all neighbours
#         Then if the neighbour is now 9, call again with new parameters
#         Return the count back to calling function
#     '''

#     if flashed == None: flashed = set()
#     # print(" >> called",r,c,flashed)

#     if (r,c) in flashed:
#         print("already flashed",r,c)
#         return

#     flashed.add((r,c))

#     for i, j in get_all_neighbours(r, c, h, w):
#         grid[i][j] += 1

#         if grid[i][j] > 9:
#             print("  >>> ",i,j)
#             flash_cascade(grid, i, j, h, w, flashed)
#             print("  <<< ",i,j)

#     return len(flashed)


def set_flashes(grid, r, c, h, w):
    # Need to ignore ones that wont flash. Without this sets all to -1 on each loop! Boom.
    if grid[r][c] <= 9:
        return

    grid[r][c] = -1

    for nr, nc in get_coords_around_all(r, c, h, w):
        if grid[nr][nc] != -1:
            grid[nr][nc] += 1
            set_flashes(grid, nr, nc, h, w)


def parse(puzzle_input):
    """Parse input"""

    with open(puzzle_input, "r") as file:
        lst = file.read().split("\n")
        lst = [[int(x) for x in row] for row in lst]

    return lst


def part1(data):
    """Solve part 1"""

    grid = data[:]
    h, w = len(grid), len(grid[0])
    flash_tally = 0

    for step in range(1, steps + 1):
        # print("Step", step)
        # print("before", grid)
        # how to do in list comprehension?
        for r, row in enumerate(grid):
            for c, vl in enumerate(row):
                grid[r][c] += 1

        for r, row in enumerate(grid):
            for c, vl in enumerate(row):
                if vl > 9:
                    set_flashes(grid, r, c, h, w)

        # print("after",grid)
        for r, row in enumerate(grid):
            for c, vl in enumerate(row):
                if vl == -1:
                    grid[r][c] = 0
                    flash_tally += 1
        # print("end",grid)
    # print("end",grid)

    return flash_tally


def part2(data):
    """Solve part 2"""

    grid = data[:]
    h, w = len(grid), len(grid[0])

    # ARGH: Lesson - The copy of data is shallow copy, its references
    # Because its a list of lists, the changes in part 1 changed the input data
    # So Part 2 is starting from end of Part 1
    # So the step counter should start from 100

    for step in range(100, 100000):
        # print("Step", step)
        # print("before", grid)
        # how to do in list comprehension?
        flash_tally = 0
        for r, row in enumerate(grid):
            for c, vl in enumerate(row):
                grid[r][c] += 1

        for r, row in enumerate(grid):
            for c, vl in enumerate(row):
                if vl > 9:
                    set_flashes(grid, r, c, h, w)

        # print("after",grid)
        for r, row in enumerate(grid):
            for c, vl in enumerate(row):
                if vl == -1:
                    grid[r][c] = 0
                    flash_tally += 1
        # print("end",grid)

        print("Flash tally at", step, " is", flash_tally)
        if flash_tally == h * w:
            break

    return step + 1


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

    tests = solve(test_file, run="Test")

    print()
    solutions = solve(soln_file)
