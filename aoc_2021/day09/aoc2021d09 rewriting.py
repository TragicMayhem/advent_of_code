# https://adventofcode.com/2021/day/9

import pathlib
import time
from collections import deque

script_path = pathlib.Path(__file__).parent
input_test = script_path / 'test.txt'  # 
input = script_path / 'input.txt'  # 
 
file_in = input #_test

grid_size_rows = 0
grid_size_cols = 0


def parse(puzzle_input):
    """Parse input - each line of 10 number signals then 4-digit number
    """

    with open(puzzle_input, 'r') as file:
        data = [[eval(x) for x in row] for row in file.read().split('\n')]
            
    return data


def get_cardinals(r, c, h, w):
    for delta_r, delta_c in ((-1, 0), (1, 0), (0, -1), (0, 1)):
        rr, cc = (r + delta_r, c + delta_c)
        if 0 <= rr < h and 0 <= cc < w:
            yield (rr, cc)


def path_search(grid, r, c, h, w):
    values_to_check = deque([(r, c)])
    visited = set()  # use set :doh: because unique, manages duplicate

    # while there are cells to visit
    while values_to_check:
        
        # get the first one in the queue and visit it
        rc = values_to_check.popleft()
        if rc in visited:
            continue

        visited.add(rc)

        # check the cardinal cells
        for nr, nc in get_cardinals(*rc, h, w):
            # check its not 9 (edge) and it is new > add to queue
            if grid[nr][nc] != 9 and (nr, nc) not in visited:
                values_to_check.append((nr, nc))

    print(visited)
    return visited

def part1(data):
    grid = data[:]

    h, w  = len(grid), len(grid[0])
    total = 0
   
    for r, row in enumerate(grid):
        for c, val in enumerate(row):

            low_point = True
            
            for neighbour_row, neighbour_col in get_cardinals(r, c, h, w):
                
                # If finds a lower neighbour then stop
                if grid[neighbour_row][neighbour_col] <= val: 
                    low_point = False
                    break

            if low_point:
                total += val + 1
                print("val+1", val+1,"tot", total)
    
    # Python way
    # for r, row in enumerate(grid):
    #     for c, cell in enumerate(row):
    #         if all(grid[nr][nc] > cell for nr, nc in get_direct_neighbours(r, c, h, w)):
    #             total += cell + 1

    return total

def part2(data):
    """Solve part 2"""   

    grid = data[:]
    sizes=[]

    h, w  = len(grid), len(grid[0])
    print("\nPart2:",w, h, grid)

    # path_search(grid, 0, 0, h, w)
    visited_coords = set()
    for r in range(h):      
        for c in range(w):
            if grid[r][c] != 9 and (r, c) not in visited_coords:
                current_coords = path_search(grid, r, c, h, w)
                # Use sets to compare and store in visited_coords.  Same as visited_coords = visited or current_coords
                visited_coords |= current_coords
                sizes.append(len(current_coords))

    sizes = sorted(sizes, reverse=True)

    return sizes[0]*sizes[1]*sizes[2]
 

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





# def part1_old(data):
#     """Solve part 1""" 

#     risk=[]
#     grid = data[:]
#     grid_size_rows = len(grid)
#     grid_size_cols = len(grid[0])

#     print(grid_size_cols, grid_size_rows, grid)

#     for r in range(grid_size_rows):
#         for c in range(grid_size_cols):
#             value=grid[r][c]
#             # print("main",r,c, "value",value,"max", grid_size_rows,grid_size_cols)

#             xposstart = 0 if r == 0 else r-1
#             yposstart = 0 if c == 0 else c-1
#             xposend = grid_size_rows if r+2 > grid_size_rows else r+2
#             yposend = grid_size_cols if c+2 > grid_size_cols else c+2

#             # print(xposstart,xposend,yposstart,yposend)
#             tally=0    
#             count=0
#             for x in range(xposstart,xposend):
#                 for y in range(yposstart,yposend):
#                     # print(x,y,"value", value, "grid[x][y]",grid[x][y])
#                     count+=1
#                     if (x, y) == (r, c):
#                         continue
#                     else:
#                         if int(value)<int(grid[x][y]):
#                             tally+=1
            
#             # print("tally", r,c,":", tally)
            
#             if tally == count-1:
#                 risk.append(int(value)+1)

#         # print(risk)
#         # print(sum(risk))

#     return sum(risk)
