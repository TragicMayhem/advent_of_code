# https://adventofcode.com/2016/day/2

import pathlib
import time

script_path = pathlib.Path(__file__).parent
input = script_path / 'input.txt'  # 92435 / C1A88
input_test = script_path / 'test.txt'  # 1985 / 5DB3

keypad_layout1 = [
    [1,2,3],
    [4,5,6],
    [7,8,9]]

keypad_layout2 = [
  [None, None, None, None, None, None, None],
  [None, None, None, 1, None, None, None],
  [None, None, 2, 3, 4, None, None],
  [None, 5, 6, 7, 8, 9, None],
  [None, None, 'A', 'B', 'C', None, None],
  [None, None, None, 'D', None, None, None],
  [None, None, None, None, None, None, None]]

max_grid_rows = len(keypad_layout2)   
max_grid_cols = len(keypad_layout2[0])   


def parse(puzzle_input):
    """Parse input """
    with open(puzzle_input, 'r') as file:
        data = file.read().split('\n')
        data = [[char for char in d] for d in data]
    return data


def convert(ch):
  '''
    Convert character (ch) to direction +ve down or right, -ve up or left
  '''
  if ch in ('D','R'): return 1
  if ch in ('U','L'): return -1
  
  return 0


def part1(data, start=(1,1)):
    """Solve part 1""" 

    pos_ud, pos_lr = start
    code = []

    for line in data:
        for char in line:
        # print('START:', ' pos ', pos_ud, pos_lr, 'Instr:', char, convert(char) )
            change = convert(char)

            if char == 'D':
                pos_ud += change
                if pos_ud > 2:  # edge bottom
                    pos_ud = 2

            elif char == 'R':  
                pos_lr += change
                if pos_lr > 2: # edge right
                    pos_lr = 2

            elif char == 'U':
                pos_ud += change
                if pos_ud < 0:  # edge top
                    pos_ud = 0

            elif char == 'L':
                pos_lr += change
                if pos_lr < 0:  # edge left
                    pos_lr = 0
            
            # print('END:', '   pos ', pos_ud, pos_lr, "Number:", keypad[pos_ud][pos_lr])
            

        code.append(keypad_layout1[pos_ud][pos_lr])
        # print('FINAL NUMBER:', keypad_layout1[pos_ud][pos_lr])
    
    ans = ''.join(str(c) for c in code)
    # print("Code:", ans)
    return ans


def part2(data, start=(3,1)):
    """Solve part 2"""

    pos_ud, pos_lr = start
    code = []

    for line in data:
        for char in line:
            # print('START:', ' pos ', pos_ud, pos_lr, 'Instr:', char, convert(char) )
            change = convert(char)
            curr_lr, curr_ud = pos_lr, pos_ud 

            if char == 'D':
                pos_ud += change
            elif char == 'R':  
                pos_lr += change
            elif char == 'U':
                pos_ud += change
            elif char == 'L':
                pos_lr += change
            
            if  keypad_layout2[pos_ud][pos_lr] == None:  # edge 
                pos_ud = curr_ud
                pos_lr = curr_lr

            # print('END:', '   pos ', pos_ud, pos_lr, "Number:", keypad_layout2[pos_ud][pos_lr])

        code.append(keypad_layout2[pos_ud][pos_lr])
        # print('FINAL NUMBER:', keypad_layout2[pos_ud][pos_lr])

    ans = ''.join(str(c) for c in code)
    # print("Code:", ans)
    return ans
 

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

    sol1, sol2, times = solve(input)
    print('\nAOC')
    print(f"Solution 1: {str(sol1)} in {times[1]-times[0]:.4f}s")
    print(f"Solution 2: {str(sol2)} in {times[2]-times[1]:.4f}s")
    print(f"\nExecution total: {times[-1]-times[0]:.4f} seconds")