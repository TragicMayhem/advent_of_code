# https://adventofcode.com/2021/day/13

import pathlib
import time

script_path = pathlib.Path(__file__).parent
input = script_path / 'input.txt'  # 655 / 
input_test = script_path / 'test.txt'  # 17 / 
 

def parse(puzzle_input):
    """Parse input """
    data = set()   # not list, to deal with unique values where dots overlap
    folds =  []

    with open(puzzle_input, 'r') as file:
        lines = [d.split(',') for d in file.read().split('\n')]

        for l in lines:
            if l[0] == '':
                continue
            
            if '=' in l[0]:
                folds.append(l[0][l[0].index('=')-1:].split('='))
                continue
            data.add((int(l[0]),int(l[1])))

        print(folds)
        # print(data)

    return data, folds


def parseV2(puzzle_input):
    """Parse input """
    # data = set()   # not list, to deal with unique values where dots overlap
    folds =  []

    with open(puzzle_input, 'r') as file:
        # This will look for the blank line in the file that separates the points and the fold instructions.
        coords, foldinstr = file.read().split('\n\n')

        # 1-line build set from tuples of each line of 'x,y' in the file (thats in coords list)
        data = set(tuple(int(x) for x in pair.split(',')) for pair in coords.split('\n'))      
        folds = list(list(x for x in instr[instr.index('=')-1:].split('=')) for instr in foldinstr.split('\n'))

    return data, folds



def isVertical(axis):
    return True if axis == 'x' else False


def foldSheet(grid,axis,foldLine):
    # print("Folding:",axis,foldLine)
    verticalFold = isVertical(axis)
    newGrid = set()

    for x, y in grid:
        # print(x,y)

        if verticalFold:
            if x > foldLine:
                x = foldLine - (x - foldLine)
        else:
            if y > foldLine: 
                y = foldLine - (y - foldLine)

        newGrid.add((x,y))

    return newGrid


def part1(d, f):
    """Solve part 1""" 
    
    # print(d, f)

    fold = f[0][0]    
    line = int(f[0][1])
    new =  foldSheet(d,fold,line)
    
    return len(new)


def showGrid(d):
    print()
    grid=list(d)

    size_x = max([position[0] for position in grid])
    size_y = max([position[1] for position in grid]) + 1

    print('Grid', size_x, 'by', size_y)

    display=[]
    for y in range(size_y+1):
        line=''
        for x in range(size_x+1):
            line += '#' if (x,y) in d else ' '
        display.append(line)

    for line in display:
        print(line)


def part2(d, f):
    """Solve part 2"""   
   
    for nextFold_axis, nextFold_line in f:
        print('Folding',nextFold_axis,nextFold_line)
        d = foldSheet(d,nextFold_axis,int(nextFold_line))
        # print(d)

    showGrid(d)

    return 1
 

def solve(puzzle_input):
    """Solve the puzzle for the given input"""
    times=[]

    data, folds = parse(puzzle_input)
    
    times.append(time.perf_counter())
    solution1 = part1(data, folds)
    times.append(time.perf_counter())
    solution2 = part2(data, folds)
    times.append(time.perf_counter())
    
    return solution1, solution2, times


def runTest(test_file):
    data, folds = parse(test_file)
    test_solution1 = part1(data, folds)
    test_solution2 = part2(data, folds)
    return test_solution1, test_solution2


def runAllTests():
    
    print("Tests")
    a, b  = runTest(input_test)
    print(f'Test1.  Part1: {a} Part 2: {b}')


if __name__ == "__main__":    # print()

    parseV2(input_test)

    runAllTests()
     
    solutions = solve(input)
    print('\nAOC')
    print(f"Solution 1: {str(solutions[0])} in {solutions[2][1]-solutions[2][0]:.4f}s")
    print(f"Solution 2: {str(solutions[1])} in {solutions[2][2]-solutions[2][1]:.4f}s")
    print(f"\nExecution total: {solutions[2][-1]-solutions[2][0]:.4f} seconds")