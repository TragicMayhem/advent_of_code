# https://adventofcode.com/2021/day/x

import pathlib
import time
import numpy as np

script_path = pathlib.Path(__file__).parent
input = script_path / 'input.txt'  # 5301 / 19492
input_test = script_path / 'test.txt'  # 35 / 3351

# 5362 too high still zero adding!!! background switching after looking at the hits on reddit

enhancements=[]

def parse(puzzle_input):
    """Parse input """

    with open(puzzle_input, 'r') as file:
        parts = file.read().split('\n\n')
    
        enhancements_converted = parts[0].replace('.','0').replace('#','1')
        enhancements = [char for char in enhancements_converted]
        # print(enhancements)

        parts[1] = parts[1].replace('.','0').replace('#','1')
        image_list = [l for l in parts[1].split('\n')]
        new_converted_image = []
        for p in image_list:
            new_converted_image.append(list(map(int,[char for char in p])))

        starter_image=np.array([np.array(xi) for xi in new_converted_image])

    return starter_image, enhancements


def get_9box(r, c):
    # Order is important for puzzle AOC 2021 D20
    for delta_r, delta_c in ((-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 0), (0, 1), (1, -1), (1, 0), (1,1)):
        rr, cc = (r + delta_r, c + delta_c)
        yield (rr, cc)


def getIntFromBin(bin_string):
    return int(bin_string,2)


def run_model(data, enhancements, iterations):
    """Solve part 1""" 
    # print(enhancements)
    # print(len(enhancements))
    # print(data)
    # print(len(data))
    # print(type(data))
    # print(np.sum(data))
    # print('='*50)


    background_flip = enhancements[0] == '1' and enhancements[-1] == '0'
    background = 0

    # need to loop x times, copy on each ones
    for count in range(iterations):
        if background_flip:
            if count % 2 == 0:
                background = 0
            else:
                background = 1

        data = np.pad(data, ((2,2),(2,2)), mode='constant', constant_values=background)
        next_image = data.copy()
        # print(next_image)

        # need to resize the image. padding is making zeros, that turn on in the main input. too high value
        # print('argmax',np.argmax(data, axis=0))
        # print('argmax',np.argmax(data, axis=1))

        for ix, iy in np.ndindex(data.shape):

            if iy == 0 or iy == len(data)-1: continue
            if ix == 0 or ix == len(data)-1: continue

            # if iy == 0 or iy == len(data)-1: continue
            # if ix == 0 or ix == len(data)-1: continue
            # print(ix,iy,'data',data[iy, ix])
            tmp=''
            for i,j in get_9box(ix,iy):
                tmp = tmp[:] + str(data[i,j])
            
            enhance_pos = getIntFromBin(tmp)
            new_value = enhancements[enhance_pos]
            next_image[ix,iy] = new_value
        
        # removing the rows and columns that are zero to get the image for next iteration
        next_image = next_image[~np.all(next_image == background, axis=1)]
        idx = np.argwhere(np.all(next_image[..., :] == background, axis=0))
        next_image = np.delete(next_image, idx, axis=1)
      
        data = next_image.copy()
        # print('sum data.copy at end', np.sum(data), 'len', len(data))
        # print(data)

    # print('-'*50)
    # print(data)
    # print(np.sum(data))
        
    return np.sum(data)


def solve(puzzle_input):
    """Solve the puzzle for the given input"""
    times=[]

    data, enhancements = parse(puzzle_input)
    
    times.append(time.perf_counter())
    solution1 = run_model(data, enhancements,2)
    times.append(time.perf_counter())
    solution2 = run_model(data, enhancements,50)
    times.append(time.perf_counter())
    
    return solution1, solution2, times


def runTest(test_file):

    data, enhancements = parse(test_file)
    test_solution1 = run_model(data, enhancements, 2)
    test_solution2 = run_model(data, enhancements, 50)
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