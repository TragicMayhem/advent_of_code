# https://adventofcode.com/2021/day/x

import pathlib
import time

script_path = pathlib.Path(__file__).parent
input = script_path / 'input.txt'  # 
input_test = script_path / 'test.txt'  # 


def parse(puzzle_input):
    """Parse input """

    with open(puzzle_input, 'r') as file:
        data = [list(d) for d in file.read().split('\n')]

    return data


EAST = '>'
SOUTH = 'v'
EMPTY = '.'


def part1(grid):
    """Solve part 1""" 

    y_size, x_size  = len(grid), len(grid[0])
    num_steps = 1

    # Check the grid for the EAST then the SOUTH but don't change anything.
    # Just log the changes to apply later, if not then need to copy the grid (unknown size)
    # every iteration (which is inefficient). If we have the grid, check for all the changes
    # then apply them after, before checking for static shape or then restarting the checks.

    while True:
        moves_to_make = []  # Reset to process EAST changes

        for y in range(y_size):
            for x in range(x_size):
                next_column = (x + 1) % x_size   # Use mod to capture the remainders and deal with the wrap around.

                if grid[y][x] == EAST and grid[y][next_column] == EMPTY:
                    moves_to_make.append((y, x, next_column))

        # process ALL the EAST moves now before looking at SOUTH
        for y, x, next_column in moves_to_make:
            grid[y][x]    = EMPTY
            grid[y][next_column] = EAST

        in_east_locked_position = not moves_to_make   # If there is something on the list, then its True.

        moves_to_make = []  # Reset for the SOUTH changes

        for y in range(y_size):
            for x in range(x_size):
                next_row = (y + 1) % y_size

                if grid[y][x] == SOUTH and grid[next_row][x] == EMPTY:
                    moves_to_make.append((y, x, next_row))

        if in_east_locked_position and not moves_to_make:  # if east locked, and now south no moves then done
            break

        for y, x, next_row in moves_to_make:
            grid[y][x]    = EMPTY
            grid[next_row][x] = SOUTH

        num_steps +=1

    return num_steps            
 

def solve(puzzle_input):
    """Solve the puzzle for the given input"""
    times=[]

    data = parse(puzzle_input)
    
    times.append(time.perf_counter())
    solution1 = part1(data)
    times.append(time.perf_counter())

    return solution1, times


def runTest(test_file):
    data = parse(test_file)
    test_solution1 = part1(data)
    return test_solution1


def runAllTests():
    
    print("Tests")
    a  = runTest(input_test)
    print(f'Test1.  Part1: {a}')


if __name__ == "__main__":    # print()

    runAllTests()

    solutions = solve(input)
    print('\nAOC')
    print(f"Solution 1: {str(solutions[0])} in {solutions[1][1]-solutions[1][0]:.4f}s")