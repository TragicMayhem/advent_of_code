# https://adventofcode.com/2016/day/4

import pathlib
import time
from collections import Counter

script_path = pathlib.Path(__file__).parent
input = script_path / 'input.txt'  # 158835 / 993
input_test = script_path / 'test.txt'  # 1514 / -


def parse(puzzle_input):
    """Parse input """
    data = []
    with open(puzzle_input, 'r') as file:
        lines = file.read().split('\n')
        for l in lines:
            a, checksum = l[:-1].split('[')
            breakup = a.split('-')
            encrypt_name = ' '.join(breakup[:-1])
            sector = int(breakup[-1])
            data.append((encrypt_name, sector, checksum)) 

    return data


def validate_rooms(rooms):
    valid_rooms = []
    
    for room in rooms:
        (name, sector, checksum) = tuple(room)
        strippedname = name.replace(' ','')
        tally = Counter(strippedname).most_common()  
        tally = sorted(tally, key=lambda m: (-m[1],m[0]))
        seq = ''.join([str(x) for x, _ in tally[:5]])
        
        if seq == checksum:
            valid_rooms.append((name, sector))
    
    return valid_rooms


def part1(data):
    """Solve part 1""" 

    # Refactors to put ina validate rooms function to reuse for Part 2
    valid_sectors = [id for _, id in validate_rooms(data)]
    return sum(valid_sectors)


def part2(data):
    """Solve part 2"""

    target_room = 'northpole object storage'
    decrypted_rooms = []

    for room in validate_rooms(data):
        name, cipher = room
        converted_room = []
        cycle = cipher % 26
        
        for c in name:
            if c == ' ':
                converted_room.append(c)
                continue
            
            if (ord(c) + cycle) <= ord('z'):
                new = ord(c) + cycle
            else:
                new = ord(c) + cycle - ord('z') + ord('a') - 1

            converted_room.append(chr(new))

        decrypted_rooms.append((''.join(converted_room), cipher))

    # print(decrypted_rooms)
    filter_object = filter(lambda a: target_room == a[0], decrypted_rooms)

    return list(filter_object)
 

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