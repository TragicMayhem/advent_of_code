# https://adventofcode.com/2015/day/xx

import pathlib
import time

script_path = pathlib.Path(__file__).parent
input = script_path / 'input.txt'           # row 3010, column 3019   result:  8997277
input_test = script_path / 'test.txt'       # row 1, column 2         result: 18749137
input_test2 = script_path / 'test2.txt'     # row 2, column 4         result:  7726640
input_test3 = script_path / 'test3.txt'     # row 4, column 5         result: 10600672

starting_val = 20151125
multiplier = 252533
modulas = 33554393


'''
   | 1   2   3   4   5   6  
---+---+---+---+---+---+---+
 1 |  1   3   6  10  15  21
 2 |  2   5   9  14  20
 3 |  4   8  13  19
 4 |  7  12  18
 5 | 11  17
 6 | 16

For example, 
the 12th code would be written to row 4, column 2; 
the 15th code would be written to row 1, column 5.
'''

def parse(puzzle_input):
    """Parse input """
    with open(puzzle_input, 'r') as file:
        data = file.read().split(',')
        target_row = int(data[0].split(' ')[-1]) - 1 
        target_col = int(data[1].split(' ')[-1]) - 1

        print("\nTarget row:", target_row, "Target column:", target_col)
    return (target_row, target_col)


def print_grid(codes):
    for r in range(len(codes)):
        for c in range(len(codes)):
            print(f"r {r} c {c} codes[{r}][{c}] {codes[r][c]}")


def process_grid(data):
    """Solve part 1""" 
    
    (target_row, target_col) = data

    grid_rows = grid_cols = target_row + target_col + 1
    codes = [[0 for i in range(grid_rows)] for j in range(grid_cols)]
    codes[0][0] = starting_val

    print("Check size of codes grid:", len(codes[0]), len(codes[1])) 
    print()

    # NOTES:
    # 1st: r0 c0 = 20151125
    # 2nd: r1 c0 > uses r0 c0 next r0 c1
    # 3rd: r0 c1 > uses r1 c0 next r2 c0
    # 4th: r2 c0 > uses r0 c1 next r1 c1
    # 5th: r1 c1 > uses r2 c0 next r0 c2
    # 6th: r0 c2 > uses r1 c1 next r3 c0

    r = 0 
    c = 0  
    previous_val = codes[0][0]

    while r != target_row or c != target_col:

        if c == 0 and r > 1:
            # print("col is zero", r, c)
            r -= 1   
            c += 1

        elif r == 0:
            # print("row is zero", r, c)
            r = c + 1
            c = 0
            
        else:  # r > 0 and c > 0
            # print("mid grid", r, c)
            r -= 1
            c += 1

        new_val = (previous_val * multiplier) % modulas
        codes[r][c] = new_val
        previous_val = new_val
        # print(f'new val = {new_val} for r({r}) c({c})')
    
    # print_grid(codes)

    answer = codes[target_row][target_col]
    # print("\nAnswer:", codes[target_row][target_col])
    return answer


def solve(puzzle_input):
    """Solve the puzzle for the given input"""
    times=[]

    data = parse(puzzle_input)
    times.append(time.perf_counter())

    solution1 = process_grid(data)
    times.append(time.perf_counter())

    return solution1, times


def runAllTests():

    print("\nTests\n")
    a, t  = solve(input_test)
    print(f'Test1: {a} in {t[1]-t[0]:.4f}s')
    a, t  = solve(input_test2)
    print(f'Test2: {a} in {t[1]-t[0]:.4f}s')
    a, t  = solve(input_test3)
    print(f'Test3: {a} in {t[1]-t[0]:.4f}s')


if __name__ == "__main__":    # print()

    runAllTests()

    sol1, times = solve(input)
    print('\nAOC')
    print(f"Solution: {str(sol1)} in {times[1]-times[0]:.4f}s")
