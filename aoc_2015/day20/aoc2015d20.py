# https://adventofcode.com/2015/day/20

import time

# Each Elf delivers presents equal to ten times his or her number at each house.
# elf 1 - every house      10 presents
# elf 7 - 7th house        70 presents
# elf 100 - 100th house    1000 presents

input = 29000000   # 665280 / 705600
input_test = 130   # 8 / 6 


def part1(target_num_presents):
    """Solve part 1""" 

    presents = []
    max_houses = target_num_presents // 4
    presents = [0] * max_houses

    for i in range(1, max_houses+1):
        num_pres = i * 10
        for j in range(i, len(presents), i):
            presents[j] += num_pres    

    for house, num_presents in enumerate(presents):
        if num_presents > target_num_presents:
            print(f"The solution is house {house} with {num_presents} presents") 
            break

    return house


def part2(target_num_presents):
    """Solve part 2"""
    max_houses_per_elf = 50   
    present_multiplier = 11

    presents = []
    limiter = target_num_presents // 4
    presents = [0] * limiter
    elves = [0] * limiter

    for i in range(1, limiter):
        num_pres = i * present_multiplier
        elves[i] = 1

        for j in range(i, len(presents), i):
            if elves[i] > max_houses_per_elf:
                break
            presents[j] += num_pres    
            elves[i] += 1

    for house, num_presents in enumerate(presents):
        if num_presents > target_num_presents:
            print(f"The solution is house {house} with {num_presents} presents") 
            break

    return house
 

def solve(puzzle_input):
    """Solve the puzzle for the given input"""
    times=[]

    times.append(time.perf_counter())

    solution1 = part1(puzzle_input)
    times.append(time.perf_counter())

    solution2 = part2(puzzle_input)
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