# https://adventofcode.com/2021/day/9

import pathlib
import time

script_path = pathlib.Path(__file__).parent
input = script_path / 'input.txt'  # 550
input_test = script_path / 'test.txt'  # 15 / 
 
file_in = input_test

grid_size_rows = 0
grid_size_cols = 0


def parse(puzzle_input):
    """Parse input - each line of 10 number signals then 4-digit number
    """

    with open(puzzle_input, 'r') as file:
        data = [list(d) for d in file.read().split('\n')]

    return data


def check_lowest_height(r, c, grid):
    '''
    '''
  
    return False



def part1(data):
    """Solve part 1""" 

    risk=[]
    grid = data[:]
    grid_size_rows = len(grid)
    grid_size_cols = len(grid[0])

    print(grid_size_cols, grid_size_rows, grid)

    for r in range(grid_size_rows):
        for c in range(grid_size_cols):
            value=grid[r][c]
            # print("main",r,c, "value",value,"max", grid_size_rows,grid_size_cols)

            xposstart = 0 if r == 0 else r-1
            yposstart = 0 if c == 0 else c-1
            xposend = grid_size_rows if r+2 > grid_size_rows else r+2
            yposend = grid_size_cols if c+2 > grid_size_cols else c+2

            # print(xposstart,xposend,yposstart,yposend)
            tally=0    
            count=0
            for x in range(xposstart,xposend):
                for y in range(yposstart,yposend):
                    # print(x,y,"value", value, "grid[x][y]",grid[x][y])
                    count+=1
                    if (x, y) == (r, c):
                        continue
                    else:
                        if int(value)<int(grid[x][y]):
                            tally+=1
            
            # print("tally", r,c,":", tally)
            
            if tally == count-1:
                risk.append(int(value)+1)

        # print(risk)
        # print(sum(risk))

    return sum(risk)


def part2(data):
    """Solve part 2"""   
         
    '''
    pop the values until 9 and add up
    if edge is not 9 tne start 0 else read untl first non-9 = start
    read along row for non 9 values = stop value
 
    grid[r].pop(0)

    '''

    sizes=[]
    grid = data[:]

    h, w  = len(grid), len(grid[0])
    print(w, h, grid)

    current_basin = []
    #check numbesr still there
    
    for r in range(h):
        print("r", grid[r])
        ix = 0  

        #if grid r 0 is 9 then stop tally and restart
        # if r is empty then skip to next
        # if grid empty stop

        if int(grid[r][0]) == 9:
            # stop counting, end of basin, reset
            basin_total = len(current_basin)
            sizes.append(basin_total)
            print("Total", basin_total)
            # break

        while ix < len(grid[r]):
            print("ix",ix,len(grid[r]),grid[r][ix])
            if int(grid[r][ix]) == 9:
                break
            
            current_basin.append(int(grid[r].pop(0)))
        
        print("Current Basin", current_basin, "len", len(current_basin))
        print("row now", grid[r])

        ## setup for non 9s and next loop


    print("Sizes",sizes)

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