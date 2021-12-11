# https://adventofcode.com/2021/day/11

import pathlib
import time
from collections import deque

script_path = pathlib.Path(__file__).parent
input = script_path / 'input.txt'  # 
input_test = script_path / 'test.txt'  # 
 
file_in = input #_test


def get_cardinals(r, c, h, w):
    for delta_r, delta_c in ((-1, 0), (1, 0), (0, -1), (0, 1)):
        rr, cc = (r + delta_r, c + delta_c)
        if 0 <= rr < h and 0 <= cc < w:
            yield (rr, cc)


def get_all_neighbours(r, c, h, w):
    for delta_r, delta_c in ((-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)):
        rr, cc = (r + delta_r, c + delta_c)
        if 0 <= rr < h and 0 <= cc < w:
            yield (rr, cc)



def flash(i, j, queue = None):
    '''
    Take the name of wire and recursively workout the set value.
    # '''
    # print("\n-----\n:")
    # if coords == None: coords = dict()

    # id = i+'-'+j

    # if id in coords.keys(): return coords.get(id)
 
    # get neighbours
    # if 9 add to queue or recurse call
    # when not 9 return

    

#   values = instructions[name]

#   if len(values) == 1:  # SET
#     # print("<1>", values)
#     tmp = convert_int(values[0])
#     wires[name] = tmp if isinstance(tmp, int) else complete_wire(tmp, wires)
       
#   elif len(values) == 2:  # NOT
#     # print("<2>", values)
#     tmp = convert_int(values[1])
#     wires[name] = ~ tmp & 0xFFFF if isinstance(tmp, int) else ~ complete_wire(tmp, wires) & 0xFFFF

#   elif len(values) == 3:  # AND, OR, LSHIFT, RSHIFT
#     # print("<3>", values)
#     left_op = convert_int(values[0])
#     right_op = convert_int(values[2]) 

#     if not isinstance(left_op, int):
#       left_op = complete_wire(left_op, wires)

#     if not isinstance(right_op, int):
#       right_op = complete_wire(right_op, wires)
      
#     if isinstance(left_op, int) and isinstance(right_op, int):
#       if "AND" in values: wires[name] = left_op & right_op
#       if "OR" in values: wires[name] = left_op | right_op
#       if "LSHIFT" in values: wires[name] = left_op << right_op
#       if "RSHIFT" in values: wires[name] = left_op >> right_op
  
#   # print("END:", wires)

    return 1



def count_flash_cascade(grid, r, c, h, w):
    
    # values_to_check = deque([(r, c)])  # Start queue off with initial coords
    # visited = set()  # use set :doh: because unique, manages duplicate

    total = 0

    # tovisit = get_all_neighbours(r,c,h,w)

    # # while there are cells to visit (checks queue automatically)
    # while values_to_check:
        
    #     # get the first one in the queue (popleft) and check if we have seen before (visited means skip)
    #     rc = values_to_check.popleft()
    #     if rc in visited:
    #         continue

    #     # If haven't visited then add to list, then check the valid cardinal cells. 
    #     # Reminder *rc is same as sending r,c (unpacks)
    #     visited.add(rc)

    for nr, nc in get_all_neighbours(r, c, h, w):
        # check its not 9 (high point of basin) and it is new > add to queue to check

        if grid[nr][nc] == 9:# and (nr, nc) not in visited:
            # get_all_neighbours ==== count flashs

            # add 1 to all neight then check again
            return flash_cascade(grid, nr,nc,h,w)

    return 0


def parse(puzzle_input):
    """Parse input"""

    with open(puzzle_input, 'r') as file:
        input = file.read().split('\n')
        input=[[int(x) for x in row] for row in input]      
    
    return input


def part1(data):
    """Solve part 1""" 

    # print(list(get_all_neighbours(3,3,5,5)))

    grid = data[:] 
    h, w  = len(grid), len(grid[0])
    flashes=0
    print(grid,"\n",h,w)

    # how to do in list comprehension?
    for r, row in enumerate(grid):
        print(row)
        for c, vl in enumerate(row):    
            grid[r][c] += 1

    flash_tally = 0
    for r, row in enumerate(grid):
        print(row)
        for c, vl in enumerate(row):    

            if vl == 9:
                for nr,nc in get_all_neighbours(r,c,h,w):
                    if grid[nr][nc] == 9:
                        flash_tally += flash_cascade(grid,r,c,h,w)
                        # cll again with this pos





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

if __name__ == "__main__":    # print()

    solutions = solve(file_in)
    print()
    print(f"Solution 1: {str(solutions[0])} in {solutions[2][1]-solutions[2][0]:.4f}s")
    print(f"Solution 2: {str(solutions[1])} in {solutions[2][2]-solutions[2][1]:.4f}s")
    print(f"\nExecution total: {solutions[2][-1]-solutions[2][0]:.4f} seconds")