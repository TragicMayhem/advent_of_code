# https://adventofcode.com/2021/day/12

from os import path
import pathlib
import time
from collections import defaultdict
from collections import deque

script_path = pathlib.Path(__file__).parent
input = script_path / 'input.txt'  # 5178
input_test = script_path / 'test.txt'  # 10 / 36
input_test2 = script_path / 'test2.txt'  #  19 / 103
input_test3 = script_path / 'test3.txt'  #  226 / 3509
 
file_in = input_test


def parse(puzzle_input):
    """Parse input """
    instr = defaultdict(list)
    with open(puzzle_input, 'r') as file:
        data = [d.split('-') for d in file.read().split('\n')]
        print(data)

        for d in data:
            instr[d[0]].append(d[1])
            if d[0] != 'start':
                instr[d[1]].append(d[0])
        
        print(instr)
    return instr    


def navigate(routes, cave, target):
    cave_q = deque([(cave,{cave})])
    # print(cave_q)
    running_total = 0

    while cave_q:

        # Get the next one and list of path options
        current, path_opts = cave_q.pop()
        # print('  Next:',current,'/',path_opts, ' q len:', len(cave_q), running_total)

        # if the current point is the target (end) then new path so count and restart
        if current == target:
            # print("  ++ at end add to path count")
            running_total+=1
            continue

        for c in routes[current]:
            # if already done the point and its lower then need to skip
            # print('loop', c)

            if c in path_opts and c.islower():
                continue
            
            # join the list of options with the next possible branch
            new_paths = path_opts.union({c}) # Could do x | y
            # print('NEW', new_paths)
            cave_q.append((c, new_paths ))

    return running_total


def navigate_extend(routes, cave, target):
    small_cave_twice = False
    cave_q = deque([(cave,{cave}, small_cave_twice)])

    print(cave_q)
    running_total = 0

    while cave_q:

        # Get the next one and list of path options and if we have already visited 2 small caves
        current, path_opts, small_cave_twice = cave_q.pop()

        print('  Next:',current,'/', path_opts, ' tot ', running_total, ' twice?', small_cave_twice)

        # if the current point is the target (end) then new path so count and restart
        if current == target:
            print("  ++ at end add to path count")
            running_total+=1
            continue

        # if already done the point and its lower then need to skip
        for c in routes[current]:
            # print('loop', c)

            # This time do the opposite, if not in list or cap then can go there, so add and then loop again
            if c not in path_opts or c.isupper():
                cave_q.append((c, path_opts | {c}, small_cave_twice ))
                continue

            if small_cave_twice:  # Means its not a new path, and we have already seen small cave twice, so need to skip
                continue

            #if here, then know its already been visited (small), and we havent broken the rule.
            # so we can just add to the stack the same list (because it has the small cave in it)
            # but set the small cave tracker to True to say we have now visited one small cave twice.
            small_cave_twice = True
            cave_q.append((c, path_opts, small_cave_twice))
            
    return running_total


def part1(data):
    """Solve part 1""" 
    # Notes: 
    # 'a' small visit 1 only. 'A' big caves visit multiple.  
    # dont want CAP-CAP edge or infinite. Can we filter out edge conditions?

    answer = navigate(data, 'start', 'end')

    return answer


def part2(data):
    """Solve part 2"""   
   
    answer = navigate_extend(data, 'start', 'end')
    print(answer)
    return answer
 

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


def test1s():
    data = parse(input_test)
    solution1 = part1(data)
    data = parse(input_test2)
    solution2 = part1(data)
    data = parse(input_test3)
    solution3 = part1(data)
    
    print(solution1)
    print(solution2)
    print(solution3)


if __name__ == "__main__":    # print()

    solutions = solve(file_in)
    print()
    print(f"Solution 1: {str(solutions[0])} in {solutions[2][1]-solutions[2][0]:.4f}s")
    print(f"Solution 2: {str(solutions[1])} in {solutions[2][2]-solutions[2][1]:.4f}s")
    print(f"\nExecution total: {solutions[2][-1]-solutions[2][0]:.4f} seconds")