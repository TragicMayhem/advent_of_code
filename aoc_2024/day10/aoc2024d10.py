# https://adventofcode.com/2024/day/10

import pathlib
import time

script_path = pathlib.Path(__file__).parent
soln_file = script_path / "input.txt"  # 472
test_file = script_path / "test.txt"  # 36
test_file2 = script_path / "test2.txt"  # 4



def get_cardinals(r, c, h, w):
    for delta_r, delta_c in ((-1, 0), (1, 0), (0, -1), (0, 1)):
        rr, cc = (r + delta_r, c + delta_c)
        if 0 <= rr < h and 0 <= cc < w:
            yield (rr, cc)


def filter_zero_height_points(points_with_height):
    """Filters a list of (point, height) tuples, returning only those with height 0.
    """
    # if (x, y)
    return [point for point, height in points_with_height if height == 0]

    # if ((x, y), h)
    # return [point for row in points_with_height for point, height in row if height == 0]


def filter_zero_height_points_from_grid(grid):
    """Filters a list of (point, height) tuples, returning only those with height 0.
    """
    zero_points = []
    for r, row in enumerate(grid):
        for c, value in enumerate(row):
            if value == 0:
                zero_points.append((r, c))
    return zero_points


def parse(puzzle_input):
    """Parse input"""

    with open(puzzle_input, "r", encoding="UTF-8") as file:
        grid = [[int(x) for x in row] for row in file.read().split("\n")]

        # grid = []
        # for y, row in enumerate(file.read().splitlines()):
        #     row_list = []
        #     for x, char in enumerate(row):
        #         height = int(char)
        #         row_list.append(((x, y), height))
        #     grid.append(row_list)
        
    print(grid)

    return grid


def count_valid_paths(grid, pos, visited=None):
    """Counts the number of valid paths from 0 to 9 in a 2D grid.
    """

    # print("\nStarting", pos, visited)

    h, w = len(grid), len(grid[0])

    if visited is None:
        visited = set()

    x, y = pos

    if x < 0 or x >= h \
    or y < 0 or y >= w \
    or (x, y) in visited:
        return 0

    if grid[x][y] == 9:
        return 1

    count = 0

    # Ensure the next step is exactly one higher
    for nx, ny in get_cardinals(x, y, h, w):
        # print("nx,ny:", nx, ny," = ", grid[nx][ny])

        if grid[nx][ny] == grid[x][y] + 1:
            # print(grid[x][y], "<" , grid[nx][ny], "len" ,len(visited))
            count += count_valid_paths(grid, (nx, ny), visited)
            visited.add((nx, ny))

    return count


def part1(data):
    """Solve part 1"""

    # h, w = len(data), len(data[0])
    # goal = 9

    trail_heads = filter_zero_height_points_from_grid(data)
    print("Trail Heads:", len(trail_heads))
    print(trail_heads)

    trail_path_count = []

    for trail_head in trail_heads:
        print("Trail Head:",trail_head)
        trail_path_count.append(count_valid_paths(data, trail_head))

    print(trail_path_count)

    return sum(trail_path_count)


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
    tests = solve(test_file2, run="Test 2")

    print()
    solutions = solve(soln_file)
