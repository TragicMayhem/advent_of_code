# https://adventofcode.com/2021/day/9

import pathlib
import time
from collections import deque

script_path = pathlib.Path(__file__).parent
soln_file = script_path / "input.txt"  # 550 / 1100682
test_file = script_path / "test.txt"  # 15 /1134

grid_size_rows = 0
grid_size_cols = 0


def parse(puzzle_input):
    """Parse input - each line of 10 number signals then 4-digit number"""

    with open(puzzle_input, "r") as file:
        data = [[eval(x) for x in row] for row in file.read().split("\n")]

    return data


def get_cardinals(r, c, h, w):
    for delta_r, delta_c in ((-1, 0), (1, 0), (0, -1), (0, 1)):
        rr, cc = (r + delta_r, c + delta_c)
        if 0 <= rr < h and 0 <= cc < w:
            yield (rr, cc)


def path_search(grid, r, c, h, w):
    values_to_check = deque([(r, c)])  # Start queue off with initial coords
    visited = set()

    # while there are cells to visit (checks queue automatically)
    while values_to_check:
        # get the first one in the queue (popleft) and check if we have seen before (visited means skip)
        rc = values_to_check.popleft()
        if rc in visited:
            continue

        # If haven't visited then add to list, then check the valid cardinal cells.
        # Reminder *rc is same as sending r,c (unpacks)
        visited.add(rc)
        for nr, nc in get_cardinals(*rc, h, w):
            # check its not 9 (high point of basin) and it is new > add to queue to check
            if grid[nr][nc] != 9 and (nr, nc) not in visited:
                values_to_check.append((nr, nc))

    # print(visited)
    return visited


def part1(data):
    grid = data[:]

    h, w = len(grid), len(grid[0])
    total = 0

    for r, row in enumerate(grid):
        for c, val in enumerate(row):
            low_point = True

            for neighbour_row, neighbour_col in get_cardinals(r, c, h, w):
                # If finds a lower neighbour then stop
                if grid[neighbour_row][neighbour_col] <= val:
                    low_point = False
                    break

            if low_point:
                total += val + 1
                # print("val+1", val+1,"tot", total)

    # Python way
    # for r, row in enumerate(grid):
    #     for c, cell in enumerate(row):
    #         if all(grid[nr][nc] > cell for nr, nc in get_direct_neighbours(r, c, h, w)):
    #             total += cell + 1

    return total


def part2(data):
    """Solve part 2"""

    grid = data[:]
    sizes = []
    h, w = len(grid), len(grid[0])

    # path_search(grid, 0, 0, h, w)
    visited_coords = set()
    for r in range(h):
        for c in range(w):
            if grid[r][c] != 9 and (r, c) not in visited_coords:
                current_coords = path_search(grid, r, c, h, w)
                # Use sets to compare and store in visited_coords.
                # Same as visited_coords = visited_coords or current_coords
                visited_coords |= current_coords
                sizes.append(len(current_coords))

    sizes = sorted(sizes, reverse=True)

    return sizes[0] * sizes[1] * sizes[2]


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
