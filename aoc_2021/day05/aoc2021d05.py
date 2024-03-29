# https://adventofcode.com/2021/day/5

import pathlib
import time

script_path = pathlib.Path(__file__).parent
soln_file = script_path / "input.txt"  #  6005 / 23864
test_file = script_path / "test.txt"  # 5 / 12
test_file2 = script_path / "test2.txt"  # 2
test_file3 = script_path / "test3.txt"  # 4
test_file4 = script_path / "test4.txt"  # 0

grid_size = 1000


def parse(puzzle_input):
    """Parse input"""

    with open(puzzle_input, "r") as file:
        lst = [line.split() for line in file]
    return lst


def part1(data):
    """Solve part 1"""
    lines = []
    grid = [[0 for j in range(grid_size)] for i in range(grid_size)]

    for d in data:
        # del(d[1])
        tmp = d[0].split(",")
        (x1, y1) = int(tmp[0]), int(tmp[1])
        tmp = d[2].split(",")
        (x2, y2) = int(tmp[0]), int(tmp[1])

        lines.append([(x1, y1), (x2, y2)])

        # print("LATEST", lines[-1])

        if (x1 == x2) or (y1 == y2):
            # print("  >> H or V line", x1, x2, y1 ,y2)

            x_str = x1 if x1 < x2 else x2
            x_end = x2 if x1 < x2 else x1

            y_str = y1 if y1 < y2 else y2
            y_end = y2 if y1 < y2 else y1

            for i in range(x_str, x_end + 1):
                for j in range(y_str, y_end + 1):
                    grid[i][j] += 1

    tally = 0

    for i in range(grid_size):
        for j in range(grid_size):
            if grid[i][j] > 1:
                tally += 1

    return tally


def part2(data):
    """Solve part 2"""
    lines = []
    grid = [[0 for j in range(grid_size)] for i in range(grid_size)]

    for d in data:
        # del(d[1])
        tmp = d[0].split(",")
        (x1, y1) = int(tmp[0]), int(tmp[1])
        tmp = d[2].split(",")
        (x2, y2) = int(tmp[0]), int(tmp[1])

        lines.append([(x1, y1), (x2, y2)])

        # print("LATEST", lines[-1])

        is_diag = abs(x1 - x2) == abs(y1 - y2)

        if (x1 <= x2 and y1 <= y2) or (x1 > x2 and y1 > y2):
            dir = 1
        else:
            dir = -1

        x_start = min(x1, x2)
        x_end = max(x1, x2)
        y_start = min(y1, y2)
        y_end = max(y1, y2)

        if (x1 == x2) or (y1 == y2) or is_diag:
            # print("  coords", (x1, y1), (x2, y2))
            # print("  >> line Using:", (x_start, y_start), (x_end, y_end), is_diag, dir)
            # print("  >> x:", x_start, "to", x_end, " y:", y_start, "to", y_end)

            if is_diag:
                j = y_start if dir == 1 else y_end

                for i in range(x_start, x_end + 1):
                    grid[j][i] += 1
                    j += 1 * dir

            else:
                for i in range(x_start, x_end + 1):
                    for j in range(y_start, y_end + 1):
                        grid[j][i] += 1

    # Use List comprehension replaces part 1 code
    tally = len([x for a in grid for x in a if x > 1])

    return tally


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
    tests2 = solve(test_file2, run="Test")
    tests3 = solve(test_file3, run="Test")
    tests4 = solve(test_file4, run="Test")

    print()
    solutions = solve(soln_file)
