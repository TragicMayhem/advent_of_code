# https://adventofcode.com/2021/day/x

import pathlib
import time

script_path = pathlib.Path(__file__).parent
input = script_path / 'input.txt'  # 571032
input_test = script_path / 'test.txt'  # 739785

player_stats = {}


def parse(puzzle_input):
    """Parse input """

    with open(puzzle_input, 'r') as file:
        p1_starts = file.readline().rstrip()[-1:]
        p2_starts = file.readline().rstrip()[-1:]

        player_stats['1'] = {'id':"Player 1",
                        'start':int(p1_starts),
                        'pos':int(p1_starts),
                        'score':0,
                        'rollcount':0,
                        'moves':[],
                        'positions':[],
                        'rolls':[]}

        player_stats['2'] = {'id':"Player 2",
                        'start':int(p2_starts),
                        'pos':int(p2_starts),
                        'score':0,
                        'rollcount':0,
                        'moves':[],
                        'positions':[],
                        'rolls':[]}


    return 1


def next_roll(number_rolls=1000):
    number = 0
    for n in range(1,number_rolls,3):
        yield n + n+1 + n+2
        # yield (n, n+1, n+2)



def part1(data):
    """Solve part 1""" 
                  
    # for n in next_roll():
    #     print(n)

    target_score = 1000
    roll_count = 0

    current_player = '1'

    while (player_stats['1']['score']<target_score and player_stats['2']['score']<target_score):

        for roll_score in next_roll():
            roll_count += 3 
         
            print('P',player_stats[current_player], 'roll', roll_score)

            print('roll_score',roll_score)
            move = roll_score % 10 if roll_score > 10 else roll_score
            print("move",move)

            tmp = (player_stats[current_player]['pos'] + move)

            new_pos = (player_stats[current_player]['pos'] + move) % 10 if tmp > 10 else tmp

            player_stats[current_player]['pos'] = new_pos
            player_stats[current_player]['score'] += player_stats[current_player]['pos']
            player_stats[current_player]['rolls'].append(roll_score)
            player_stats[current_player]['positions'].append(new_pos)
            player_stats[current_player]['moves'].append(move)

            if player_stats['1']['score'] >= target_score:
                break
            
            if player_stats['2']['score'] >= target_score:
                break

            current_player = '2' if current_player == '1' else '1'


        print(player_stats['1'])
        print(player_stats['2'])
        print('roll count', roll_count)

        lowest_score = min(player_stats['1']['score'],player_stats['2']['score'])
        answer = lowest_score * roll_count

    return answer


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