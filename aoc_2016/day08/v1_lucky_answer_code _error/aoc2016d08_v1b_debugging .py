# https://adventofcode.com/2015/day/8

from itertools import count
import pathlib
from socketserver import DatagramRequestHandler
import time
from pprint import pprint as pp

script_path = pathlib.Path(__file__).parent
input = script_path / 'input.txt'       # 121 / RURUCEOEIL
input_test = script_path / 'test.txt'   # 6 / -

# todo - there are # missing from the printout and the count is 117 (count #) compared to 121 (count rect values)
# This MUST be wrong. need to check the rotate and work out which is failing > Guessing column

SCREEN_WIDTH = 50
SCREEN_HEIGHT = 6


def test_functions():
    print('TESTING FUNCTIONS')
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
    print('-'*50)


def parse(puzzle_input):
    """Parse input 
    Input variation:
        rect 3x2
        rotate column x=1 by 1
        rotate row y=0 by 4
    """
    with open(puzzle_input, 'r') as file:
        lines = file.read().split('\n')
        data = tuple()

        for l in lines:
            instruction = l.split()
            if instruction[0] == 'rect':
                x , y = tuple(l[5:].split('x'))
                data = data + (('rect', int(x), int(y)), )
            else:  # 'rotate'
                data = data + ((instruction[1], int(instruction[2][2:]), int(instruction[4])), )
    
    # print(data)
    return data


def fill_in_rect(grid, w, h):
    # print('fill_in_rect(grid, w, h)', w, h)
    for r in range(h):
        grid[r] = ['#'] * w + grid[r][w:]

    return grid


def rotate_row(grid, row, pixels):
    # print('rotate_row(grid, row, pixels)', row, pixels)
    
    pixels = pixels % len(grid[row])
    grid[row] = grid[row][-pixels:] + grid[row][:-pixels]

    return grid


def rotate_column(grid, col, pixels):
    print('rotate_column(grid, col, pixels)', col, pixels)
    

    # not sure it works when its 1
    print('   a', pixels)
    pixels = pixels % len(grid)
    print('   b',pixels)
    
    tmp_column = []

    show_screen(grid)

    for row in range(len(grid)):
        tmp_column.append(grid[row][col])
    
    print("tmp before:", tmp_column)
    tmp_column = tmp_column[-pixels:] + tmp_column[:-pixels]
    print("tmp after :", tmp_column)

    print(len(tmp_column))

    for row in range(len(grid)):
        print(row, col)
        val = tmp_column.pop(0)
        print(val, len(tmp_column), tmp_column)
        grid[row][col] = val # tmp_column.pop(0)
        print('grc', grid[row][col])
        print('gr_', grid[row])
        print(grid)

    print(grid)
    show_screen(grid)

    return grid


def generate_screen(width, height):
    grid = [['.'] * width] * height
    return grid


def show_screen(grid):
    print()
    for line in grid:
        print(' '.join(line).replace('.', ' '))   
    print()


def process_screen(data, w, h):
    """Solve part 1""" 
   
    grid = generate_screen(w, h)
    count_on = 0 

    for d in data:
        print('Instruction:', d)
        if d[0] == 'rect':
            grid = fill_in_rect(grid, d[1], d[2])
            count_on += d[1] * d[2]
        
        elif d[0] == 'row':
            grid = rotate_row(grid, d[1], d[2] )
        
        elif d[0] == 'column':
            grid = rotate_column(grid, d[1], d[2] )

        print("processing count_on:", count_on)
        print('  grid check        :',sum(x.count('#') for x in grid))

    show_screen(grid)

    # To answer part 1 - anything that draws a rectangle must turn on lights. Just count them.
    print('Sum of rect w*h:', count_on)
    
    print('question is - why does the count of all the # not equal the above. # missing from the letter!')
    print(sum(x.count('#') for x in grid))

    return count_on

def solve(puzzle_input, w = SCREEN_WIDTH, h = SCREEN_HEIGHT):
    """Solve the puzzle for the given input"""
    times=[]

    data = parse(puzzle_input)
    times.append(time.perf_counter())

    solution1 = process_screen(data, w, h)
    times.append(time.perf_counter())
    
    return solution1, times


def runAllTests():

    print("\nTests\n")
    a, t  = solve(input_test, 7, 3)
    print(f'Test1 Part 1: {a} in {t[1]-t[0]:.4f}s')
    print(f"      Execution total: {t[-1]-t[0]:.4f} seconds")


if __name__ == "__main__":    # print()

    # test_functions()
    # runAllTests()

    sol1, times = solve(input)
    print('\nAOC')
    print(f"Solution: {str(sol1)} in {times[1]-times[0]:.4f}s")
    print(f"\nExecution total: {times[-1]-times[0]:.4f} seconds")