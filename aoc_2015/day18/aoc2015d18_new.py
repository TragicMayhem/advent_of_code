# https://adventofcode.com/2015/day/18

import pathlib
from sys import setprofile
import time
import copy
from pprint import pprint

script_path = pathlib.Path(__file__).parent
input = script_path / 'input.txt'  # 821 / 
input_test = script_path / 'test_part1.txt'  # 4
input_test2 = script_path / 'test_part2.txt'  #


def parse(puzzle_input):
    """Parse input """
    with open(puzzle_input, 'r') as file:
        lights_grid = [list(map(lambda ele: True if ele == '#' else False, d)) for d in file.read().split('\n')]
    return lights_grid


## needs to be for max grid size, pass in grid len?
def corner(x, y): return (x,y) in [(0,0),(0,99),(99,0),(99,99)]


def lockCorners():

    return 1


def get_coords8d(r, c, h, w):
    for delta_r, delta_c in ((-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)):
        rr, cc = (r + delta_r, c + delta_c)
        if 0 <= rr < h and 0 <= cc < w:
            yield (rr, cc)


def next_state(grid, grid_size, posx, posy):
    '''
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
    '''
    current_status = grid[posx][posy]

    lights_on = sum(filter(None, [grid[x][y] for x,y in get_coords8d(posx, posy, grid_size, grid_size)]))

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
        new_state_grid = []

        for i in range(grid_size):
            tmp = []
            for j in range(grid_size):
                tmp.append(next_state(lights, grid_size, i, j)) 
            
            new_state_grid.append(tmp)

        # print(f"State {step+1} has {sum([sum(d) for d in new_state_grid])} lights on")
        # lights = copy.deepcopy(new_state_grid)
        lights = new_state_grid

    answer = sum([sum(d) for d in lights])

    return answer


def part2(data, steps=100):
    """Solve part 2"""

    return 1


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
    data = parse(input_test)
    test_solution1 = part1(data, 4)
    data = parse(input_test2)
    test_solution2 = part2(data, 5)

    print(f'Test1.  Part1: {test_solution1} Part 2: {test_solution2}')


if __name__ == "__main__":    # print()

    runAllTests()

    solutions = solve(input)
    print('\nAOC')
    print(f"Solution 1: {str(solutions[0])} in {solutions[2][1]-solutions[2][0]:.4f}s")
    print(f"Solution 2: {str(solutions[1])} in {solutions[2][2]-solutions[2][1]:.4f}s")
    print(f"\nExecution total: {solutions[2][-1]-solutions[2][0]:.4f} seconds")
