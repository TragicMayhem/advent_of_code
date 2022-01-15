# https://adventofcode.com/2016/day/3

import pathlib
import time

script_path = pathlib.Path(__file__).parent
input = script_path / 'input.txt'  # 1050 (942 impossible) / 1921
input_test = script_path / 'test.txt'  # 5 (4 impossible)


def parse(puzzle_input):
    """Parse input """
    with open(puzzle_input, 'r') as file:
        data = file.read().split('\n')  # Read file make list by splitting on new line \n
        data = [' '.join(d.split()).split() for d in data] # Splits/rejoins (to replace the multiple spaces), the splits into list
        data = [[int(i) for i in d] for d in data]  
    return data


def part1(data):
    """Solve part 1""" 

    impossible = []
    valid = []

    for triangle in data:
        if len(triangle) == 3:
            combi1 = triangle[0] + triangle[1] > triangle[2]
            combi2 = triangle[0] + triangle[2] > triangle[1]
            combi3 = triangle[1] + triangle[2] > triangle[0]
            valid_triangle = all([combi1, combi2, combi3])

            # print(f'Tri: {triangle}, {combi1} {combi2} {combi3} >>> Status = {valid_triangle}')

            if valid_triangle:
                valid.append(triangle)
            else:
                impossible.append(triangle)
      
        else:
            print("Incorrect number of sides)")
  
    print(f"Input: {len(data)} with {len(valid)} valid triangles and {len(impossible)} impossible")

    return len(valid)


def tri_validity(sides):
    if isinstance(sides, tuple) and len(sides) == 3:
        side1, side2, side3 = sides
    else:
        side1 = side2 = side3 = 0 

    combi1 = side1 + side2 > side3
    combi2 = side1 + side3 > side2
    combi3 = side2 + side3 > side1
    
    return all([combi1, combi2, combi3])


def build_tri(g1, g2 ,g3):
    if not(isinstance(g1, list) and isinstance(g2, list) and isinstance(g3, list) and \
        len(g1) == 3 and len(g2) == 3 and len(g3) == 3):
        return [(),(),()]
    
    t1 = (g1[0], g2[0], g3[0])
    t2 = (g1[1], g2[1], g3[1])
    t3 = (g1[2], g2[2], g3[2])
    
    return [t1, t2, t3]


def part2(data):
    """Solve part 2"""

    impossible = []
    valid = []

    for i in range(0,len(data),3 ):
        # print(i)
        tri1, tri2, tri3 = build_tri(data[i], data[i+1], data[i+2])
        # print(f'Tri: {tri1} >>> Status = {tri_validity(tri1)}')
        # print(f'Tri: {tri2} >>> Status = {tri_validity(tri2)}')
        # print(f'Tri: {tri3} >>> Status = {tri_validity(tri3)}')

        valid.append(tri1) if tri_validity(tri1) else impossible.append(tri1)   
        valid.append(tri2) if tri_validity(tri2) else impossible.append(tri2)   
        valid.append(tri3) if tri_validity(tri3) else impossible.append(tri3)   
    
    print()
    print(f"Input: {len(data)} with {len(valid)} valid triangles and {len(impossible)} impossible")

    return len(valid)
 

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