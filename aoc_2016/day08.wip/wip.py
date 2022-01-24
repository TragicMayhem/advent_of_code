# https://adventofcode.com/2015/day/8

import pathlib
import time
from pprint import pprint as pp

script_path = pathlib.Path(__file__).parent
input = script_path / 'input.txt'  #
input_test = script_path / 'test.txt'  # 

SCREEN_WIDTH = 50
SCREEN_HEIGHT = 6

def parse(puzzle_input):
    """Parse input 
    Input variation:
        rect 3x2
        rotate column x=1 by 1
        rotate row y=0 by 4

    """
    with open(puzzle_input, 'r') as file:
        data = file.read().split('\n')

    
    g = fill_in_rect(generate_screen(10,4), 5, 4)
    pp(g)
    g = rotate_row(g, 0, 1)
    g = rotate_row(g, 1, 2)
    g = rotate_row(g, 2, 5)
    g = rotate_row(g, 3, 6)
    pp(g)
    g = rotate_column(g, 1, 1)
    pp(g)
    g = rotate_column(g, 3, 2)
    pp(g)
    g = rotate_column(g, 7, 2)
    pp(g)
    g = rotate_column(g, 9, 5)
    pp(g)

    return data


def fill_in_rect(grid, w, h):
    print('fill_in_rect(grid, w, h)', w, h)

    for r in range(h):
        grid[r] = ['#'] * w + grid[r][w:]

    return grid


def rotate_row(grid, row, pixels):
    print('rotate_row(grid, row, pixels)', row, pixels)
    
    pixels = pixels % len(grid[row])
    grid[row] = grid[row][-pixels:] + grid[row][:-pixels]

    return grid


def rotate_column(grid, col, pixels):
    print('rotate_column(grid, col, pixels)', col, pixels)
    
    pixels = pixels % len(grid)
    
    tmp_column = []
    for row in range(len(grid)):
        tmp_column.append(grid[row][col])
 
    tmp_column = tmp_column[-pixels:] + tmp_column[:-pixels]

    for row in range(len(grid)):
        grid[row][col] = tmp_column.pop(0)

    return grid



def generate_screen(width = SCREEN_WIDTH, height = SCREEN_HEIGHT):
    grid = [['.'] * width] * height
    return grid


def part1(data):
    """Solve part 1""" 
   
    return 1


def part2(data):
    """Solve part 2"""
    
    return 1
 

def solve(puzzle_input):
    """Solve the puzzle for the given input"""
    times=[]

    data = parse(puzzle_input)
    times.append(time.perf_counter())

    solution1 = part1(data)
    times.append(time.perf_counter())

    solution2 = part2(data)
    times.append(time.perf_counter())
    
    return solution1, solution2, times


def runAllTests():

    print("\nTests\n")
    a, b, t  = solve(input_test)
    print(f'Test1 Part 1: {a} in {t[1]-t[0]:.4f}s')
    print(f'      Part 2: {b} in {t[2]-t[1]:.4f}s')
    print(f"      Execution total: {t[-1]-t[0]:.4f} seconds")


if __name__ == "__main__":    # print()

    runAllTests()

    # sol1, sol2, times = solve(input)
    # print('\nAOC')
    # print(f"Solution 1: {str(sol1)} in {times[1]-times[0]:.4f}s")
    # print(f"Solution 2: {str(sol2)} in {times[2]-times[1]:.4f}s")
    # print(f"\nExecution total: {times[-1]-times[0]:.4f} seconds")