# https://adventofcode.com/2015/day/18

import pathlib
import time
import copy

script_path = pathlib.Path(__file__).parent
input = script_path / "input.txt"  # (after 100 steps) 821 / 886
input_test = (
    script_path / "input_test.txt"
)  # 4 (after 4 steps) / 14 (after 4 steps)  (or in example 17 after 5 steps)


def parse(puzzle_input):
    """Parse input"""
    with open(puzzle_input, "r") as file:
        lights_grid = [
            list(map(lambda ele: True if ele == "#" else False, d))
            for d in file.read().split("\n")
        ]
    return lights_grid


def get_coords8d(r, c, size):
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
        if 0 <= rr < size and 0 <= cc < size:
            yield (rr, cc)


def next_state(grid, grid_size, posx, posy):
    """
    Updates lights based on neighbours status
    On: Stays on if 2 or 3 neighbours on else off.
    Off: Turns on if 3 neighbours on, else stays off
    Edges (assume off)

    Parameters:
      x (int): row of the grid
      y (int): column of the grid
      [][] (bool): Grid with True/False

    Returns:
      next state (Bool):  True (on) False (off)
    """
    current_status = grid[posx][posy]

    lights_on = sum(
        filter(None, [grid[x][y] for x, y in get_coords8d(posx, posy, grid_size)])
    )

    if current_status and 2 <= lights_on <= 3:
        return True

    if not current_status and lights_on == 3:
        return True

    return False


def part1(lights, steps=100):
    """Solve part 1"""

    # print(lights_grid)
    grid_size = len(lights)
    # print("START lights on:", sum([sum(d) for d in lights]))

    for step in range(steps):
        new_state_grid = [None] * grid_size
        for i in range(grid_size):
            tmp = []
            for j in range(grid_size):
                tmp.append(next_state(lights, grid_size, i, j))
            new_state_grid[i] = tmp
        # pprint(new_state_grid)

        # print(f"State {step+1} has {sum([sum(d) for d in new_state_grid])} lights on")
        lights = copy.deepcopy(new_state_grid)

    answer = sum([sum(d) for d in lights])

    return answer


## PART 2 ##


def change_state(lights_on, size, coords):
    """
    Updates lights based on neighbours status
    On: Stays on if 2 or 3 neighbours on else off.
    Off: Turns on if 3 neighbours on, else stays off
    Edges (assume off)

    Parameters:
      x (int): row of the grid
      y (int): column of the grid
      [][] (bool): Grid with True/False

    Returns:
      next state (Bool):  True (on) False (off)
    """
    current_status = coords in lights_on
    (x, y) = coords

    if coords in ({(0, 0), (0, size - 1), (size - 1, 0), (size - 1, size - 1)}):
        # print('corner keeping on')
        return True

    how_many_on_around = sum(
        filter(None, [(x, y) in lights_on for x, y in get_coords8d(x, y, size)])
    )

    if (
        current_status and 2 <= how_many_on_around <= 3
    ):  # ON already with 2 to 3 around = stays ON
        return True

    if (
        not current_status and how_many_on_around == 3
    ):  # OFF already with exactly 3 on around = turns ON
        return True

    return False


def part2(lights, steps=100):
    """Solve part 2"""

    grid_size = len(lights)

    lights_on = set()
    corners = {
        (0, 0),
        (0, grid_size - 1),
        (grid_size - 1, 0),
        (grid_size - 1, grid_size - 1),
    }

    # build initial for now
    for i in range(grid_size):
        for j in range(grid_size):
            if lights[i][j]:
                lights_on.add((i, j))
    lights_on.update(corners)  # Make sure corners are on

    for step in range(steps):
        tmp_lights = lights_on.copy()

        for row in range(grid_size):
            for col in range(grid_size):
                if change_state(lights_on, grid_size, (row, col)):
                    tmp_lights.add((row, col))
                else:
                    tmp_lights.discard((row, col))

        # print(f"After step {step+1} has {len(tmp_lights)} lights on")
        lights_on = tmp_lights.copy()

    return len(lights_on)


def solve(puzzle_input, steps=100):
    """Solve the puzzle for the given input"""
    times = []

    data = parse(puzzle_input)

    times.append(time.perf_counter())

    solution1 = part1(data, steps)
    times.append(time.perf_counter())

    solution2 = part2(data, steps)
    times.append(time.perf_counter())

    return solution1, solution2, times


def runAllTests():
    print("\nTests\n")
    a, b, t = solve(input_test, 4)
    print(f"Test1 Part 1: {a} in {t[1]-t[0]:.4f}s")
    print(f"      Part 2: {b} in {t[2]-t[1]:.4f}s")
    print(f"      Execution total: {t[-1]-t[0]:.4f} seconds")


if __name__ == "__main__":  # print()
    runAllTests()

    sol1, sol2, times = solve(input, 100)
    print("\nAOC")
    print(f"Solution 1: {str(sol1)} in {times[1]-times[0]:.4f}s")
    print(f"Solution 2: {str(sol2)} in {times[2]-times[1]:.4f}s")
    print(f"\nExecution total: {times[-1]-times[0]:.4f} seconds")
