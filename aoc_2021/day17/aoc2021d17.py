# https://adventofcode.com/2021/day/x

from os import curdir
import pathlib
import time
import re

script_path = pathlib.Path(__file__).parent
input = script_path / 'input.txt'  # 
input_test = script_path / 'test.txt'  # 

re_pattern = '.*x=(-?\d+)\.{2}(-?\d+), y=(-?\d+)\.{2}(-?\d+)'


def num_groups(regex):
    return re.compile(regex).groups


def parse(puzzle_input):
    """Parse input
       target area: x=20..30, y=-10..-5"""
    
    with open(puzzle_input, 'r') as file:
        line = file.readline()
        res = re.search(re_pattern,line)

        if res:
            target = [int(x) for x in res.groups()]       #  map?
      
    return tuple(target)


def delta_change(dx, dy, step):
    
    new_dx = dx - step if dx > 0 else 0
    new_dy = dy - step

    return (new_dx, new_dy)


# def new_location(cx, cy, dx, dy):
    
#     new_dx = dx - 1 if dx > 0 else 0
#     new_dy = dy - 1
    
#     new_x = cx + dx
#     new_y = cy + dy

#     return (new_x, new_y)


def part1(data):
    """Solve part 1""" 
    
    (target_x1, target_x2, target_y1, target_y2) = data
   
    # target_xsize = abs(target_x1 - target_x2)
    # target_ysize = abs(target_y1 - target_y2)
    # print("target size",target_xsize, target_ysize)

    # y2 wrong: print(-73 * (-73 + 1) / 2)  # not 2628
    # y1 right: print(-98 * (-98 + 1) / 2)  # 4753
    ans = int(target_y1 * (target_y1 + 1) / 2)

    return ans


# copy and paste first attempt to work out logic and then rationalize 
# (trial and error with a little math!)

    # target_xsize = abs(target_x1 - target_x2)
    # target_ysize = abs(target_y1 - target_y2)
    # print("target size",target_xsize, target_ysize)
 
            # while tracking and step_count<50:

            #     dx, dy = delta_change(dx, dy, step_count)

            #     x_pos, y_pos = (x_pos + dx, y_pos + dy)
            #     print("current", x_pos, y_pos)

            #     if y_pos > max_y:   #  track highest y value
            #         print("New heights", y_pos)
            #         max_y = y_pos

            #     if x_pos == 0 and x_pos < target_x1:
            #         print("Falling short.....")
            #         tracking=False
            #         break

            #     if y_pos > target_y2:
            #         print("Below target.....")
            #         tracking=False
            #         break

            #     if x_pos > target_x2 and y_pos < target_y1:
            #         print("Overshot.....")
            #         tracking=False
            #         break

            #     if target_x1 <= x_pos <= target_x2:
            #         print("In X zone")
                    
            #         if (y_pos > target_y2):
            #             print("Undershot.....")
            #             tracking=False
            #             break

            #     if target_x1 <= x_pos <= target_x2 and \
            #         target_y1 <= y_pos <= target_y2:  # careful of negative, might need to check this
            #         print("--- in target ---")
            #         tracking = True
            #         winning_results.append(((x,y),max_y))
            #         break

            #     if x_pos < target_x1 and y_pos > target_y1:
            #         pass

            #     if abs(y_pos) > abs(target_y2):
            #         pass

            #     if abs(y_pos) < target_y1 and x_pos > target_x2:
            #         pass

            #     step_count += 1

def part2(data):
    """Solve part 2"""   
   
    (target_x1, target_x2, target_y1, target_y2) = data
    # print("Data",data)

    start = (0,0)
    winning_results = []

    # These two loops (x,y) are trying the combincations of trajectory
    for dx in range(0, target_x2+1):
        # fire towards target and getting slower (x)
        # print("x:", dx)

        max_y = 0
        
        # for y in range(0, target_y1*10):  
        for dy in range(target_y1, -target_y1):  
            # not right for parabola - do we need to start at target y? negatives?
            # fire up (or down?) and gravity affects pulling down
            # print("Start combination x,y:", dx, dy)

            # track the y.  if going up good, if going down stop.  cause got to the highest. how?
            step_count = 1
            x_pos, y_pos = start
            
            # prev_y = 0
            combi = (dx, dy)  # initial delta
            current_dx = dx
            current_dy = dy
            

            while x_pos <= target_x2 and y_pos >= target_y1: # or y2?
                # print(current_dx, current_dy)

                if y_pos > max_y:   #  track highest y value
                    # print("New heights", y_pos)
                    max_y = y_pos

                if target_x1 <= x_pos <= target_x2 and \
                    target_y1 <= y_pos <= target_y2:  # careful of negative, might need to check this
                    # print("--- in target ---")
                    winning_results.append(((dx,dy),max_y))
                    break

                x_pos += current_dx
                y_pos += current_dy

                current_dy -= 1 
                current_dx = current_dx - 1 if current_dx > 0 else 0
           


    # print("Winning vectors\n",winning_results)

    how_many_winning_vectors = len(winning_results)

    #Answers for Part 1 without using the simple math formula (thats not fool proof)
    whats_the_highest_y = max(winning_results,key=lambda item:item[1])[1]
    whats_the_vector_for_highest_y = max(winning_results,key=lambda item:item[1])[0]
    
    return how_many_winning_vectors

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


def runTest(test_file):
    data = parse(test_file)
    test_solution1 = part1(data)
    test_solution2 = part2(data)
    return test_solution1, test_solution2


def runAllTests():
    
    print("Tests")
    a, b  = runTest(input_test)
    print(f'Test1.  Part1: {a} Part 2: {b}')


if __name__ == "__main__":    # print()

    runAllTests()

    solutions = solve(input)
    print('\nAOC')
    print(f"Solution 1: {str(solutions[0])} in {solutions[2][1]-solutions[2][0]:.4f}s")
    print(f"Solution 2: {str(solutions[1])} in {solutions[2][2]-solutions[2][1]:.4f}s")
    print(f"\nExecution total: {solutions[2][-1]-solutions[2][0]:.4f} seconds")