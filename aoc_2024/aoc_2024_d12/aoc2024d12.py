# https://adventofcode.com/2024/day/12

import pathlib
import time

script_path = pathlib.Path(__file__).parent
soln_file = script_path / "input.txt"  #
test_file = script_path / "test.txt"  # 140
test_file2 = script_path / "test2.txt"  # 772
test_file3 = script_path / "test3.txt"  # 1930


def parse(puzzle_input):
    """Parse input"""

    with open(puzzle_input, "r", encoding="UTF-8") as file:
        grid = [[x for x in row] for row in file.read().split("\n")]

    print(grid)

    return grid

def get_cardinals(r, c, h, w):
    for delta_r, delta_c in ((-1, 0), (1, 0), (0, -1), (0, 1)):
        rr, cc = (r + delta_r, c + delta_c)
        if 0 <= rr < h and 0 <= cc < w:
            yield (rr, cc)


def explore_region(grid, x, y, letter, visited):
    if (x, y) in visited:
        return 0, 0

    visited.add((x, y))
    size = 1
    perimeter = 4

    # Check neighbors and adjust perimeter
    for nx, ny in get_cardinals(x, y, len(grid), len(grid[0])):

        if grid[nx][ny] == letter:
            inner_size, inner_perimeter = explore_region(grid, nx, ny, letter, visited)
            size += inner_size
            perimeter -=1
            # perimeter += inner_perimeter
        else:
            perimeter += 1

    return size, perimeter


def part1(grid):
    """Solve part 1"""
    h = len(grid)
    w = len(grid[0])
    visited = set()
    regions = []

    for i in range(h):
        for j in range(w):
            if (i, j) not in visited:
                size, perimeter = explore_region(grid, i, j, grid[i][j], visited)
                regions.append((size, perimeter))

    print(regions)

    return 1


def part2(data):
    """Solve part 2"""

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

    tests = solve(test_file, run="Test")

    print()
    # solutions = solve(soln_file)
