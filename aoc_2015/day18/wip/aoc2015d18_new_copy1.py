# https://adventofcode.com/2015/day/18

import pathlib
from sys import setprofile
import time
import copy
from pprint import pprint

script_path = pathlib.Path(__file__).parent
input = script_path / 'input.txt'  #
input_test = script_path / 'test_part1.txt'  #
input_test2 = script_path / 'test_part2.txt'  #


def parse(puzzle_input):
    """Parse input """

    with open(puzzle_input, 'r') as file:
        data = file.read().split('\n')
        data = [list(d) for d in data]

        lights_grid = []
        for d in data:
            res = list(map(lambda ele: True if ele == '#' else False, d))
            lights_grid.append(res)

    return lights_grid


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
    neighbours = []

    for x in range(posx-1, posx+2):
        if x < 0 or x > grid_size-1:
            continue
        for y in range(posy-1, posy+2):
            if y < 0 or y > grid_size-1 or (posx, posy) == (x, y):
                continue
            neighbours.append((x, y))

    neighbours_state = []
    for x, y in neighbours:
        neighbours_state.append(grid[x][y])

    lights_on = sum(neighbours_state)
    lights_off = len(neighbours_state) - lights_on

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
