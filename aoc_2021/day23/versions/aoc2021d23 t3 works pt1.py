# https://adventofcode.com/2021/day/23

import pathlib
import time
from math import inf as INF
from functools import lru_cache

script_path = pathlib.Path(__file__).parent
input = script_path / 'input.txt'  # 
input_test = script_path / 'test.txt'  # 12521

'''
NOTES
hallway is 11 long - actually 7 if they cannot stop in the space outside room
4 rooms each 2 spaces
rooms L-R target is to hold A-B-C-D

7 holding spaces
8 spaces in rooms
8 target spaces

A cost 1
B cost 10
C cost 100
D cost 1000 

need to know each status for the rules
- locked hallway (after moving there, then waiting for their room)
- not in target
- still in start room
- hasnt moved yet, allowed to stay in rooms
- once in a hallway, wont move unless their room is free (target room)
- cant wait in space outside the rooms (effectively blocked?)
- cant go into a room if there is one already not in final place
- need to count number of moves with each. unique id

- if pos in source room, is low(1), and not target room,     need to move before target can move in 

'''

# do by letter / strings and tuple of valid positions in the hall (not outside room)
# target_layout = ('AA','BB','CC','DD')
# hallway = '...........'
# valid_hallway_idn = (0,1,3,4,7,9,10)   # Not in the spaces outside the rooms


'''
## Completing AFTER Christmas (26th Dec) - Notes on research
##
## OK this one makes my brain hurt, I have read hints pages, and now 5 or 6 other peoples code (including in other languages) - so many different approaches
## I almost get a few of them (ones that comment to help noobs lik me!) 
## this one I have hacked my code to adapt to a way of thinking using tuples and yield - main reason, I don't get this in 
## python so I am using it to practice implementation of DFS, recursion, tuples and using yield generators.
'''

hallway_spaces = (None, None, None, None, None, None, None)  # 7 slots - 2 each edge then 3 in between rooms   (None,) * 7
room_answer = [(0,0), (1,1), (2,2), (3,3)]

# After reading hints the costs are 10 to power x where x is 0,1,2,3 
# which is good if you are indexing tuple and therefore translate ABCD to 0123

COSTS = {
    'A' : 1,     #10^0
    'B' : 10,    #10^1
    'C' : 100,   #10^2
    'D' : 1000   #10^3
}

# distance from  room to hallway location is to use a map tuples), index by room and hall index gives steps
# plus need to take account of position in the room
ROOM_DISTANCE = (
    (2, 1, 1, 3, 5, 7, 8), # from/to room 0
    (4, 3, 1, 1, 3, 5, 6), # from/to room 1
    (6, 5, 3, 1, 1, 3, 4), # from/to room 2
    (8, 7, 5, 3, 1, 1, 2), # from/to room 3
)


def parse(puzzle_input):
    """Parse input """

    with open(puzzle_input, 'r') as file:
        data = file.read().split('\n')
        
        rooms = []
        # Ignore the hallway, only interested in who is starting in which room
        # The rooms are at character: 3, 5, 7, 9
        for line in data[2:4]:
            # So turns out doing lots of if statements, and lookup function all gets replaced by this ONE line
            # this uses the string index function to return the index position in the given string (which is 'ABCD')
            # this returns 0, 1, 2, 3 like the rooms .   VERY CLEVER (to me) - store somewhere for later!
            # So using the map function with the string index, mapping over a tuple of the room positions gives you
            # a list of the 4 amphipods (changed from ABCD to 0123)
            # print(list(map('ABCD'.index, (line[3], line[5], line[7], line[9]))))
            rooms.append(list(map('ABCD'.index, (line[3], line[5], line[7], line[9]))))

        # so rooms is a list of lists (only 2).  They are four 0123*2 across the two lists
        # zip will take the first element of each list and put in group together, then the 2nd, 3rd, 4th - this builds the
        # starting room groupings.  *rooms unpacks the lists for the zip (which is an object) and then list makes it a list

        '''
        ###B#C#B#D###
        [1, 2, 1, 3]
          #A#D#C#A#
        [0, 3, 2, 0]
        [(1, 0), (2, 3), (1, 2), (3, 0)]
        '''

        data = tuple(zip(*rooms))
        # print(data)

    return data


def move_to_room(all_rooms, hall):
    # print('move to room', all_rooms, hall)

    # Check the hallway for pods
    for h_idx, location  in enumerate(hall):
        # print('M2R loop', h_idx, location)
        
        if location == None:  # is None
            # Means its free/empty so could use/walk through
            continue
 
        # Means there is a pod in this location in the hall
        # that will be a number 0-3 to index the rooms
        single_room = all_rooms[location]
        
        check_same = True  # Assume same type in the room
        for occupant in single_room:
            if occupant != location:  # If they don't match then cannot move
                check_same = False
                break

        if not check_same:
            continue

        # for the above could have used "if any(occupant != pod for occupant in room):

        # work out the cost
        cost = calculate_cost_to_move(single_room, hall, location, h_idx, into_room=True)

        if cost == INF:
            continue

        # need to work out the new room and hallway if this pod as moved
        # To generate a one-element tuple, a comma , is required at the end.
        # If you want to add only one element, you can concatenate a tuple with one element. t_add_one = t + (3,)
        changed_rooms = all_rooms[:location] + ((location,) + single_room,) + all_rooms[location + 1:]
        changed_hall = hall[:h_idx] + (None,) + hall[h_idx + 1:]

        # print("all", all_rooms,"changed", changed_rooms)
        # print("Hall", hall,"changed hall", changed_hall)

        yield cost, (changed_rooms, changed_hall)


def move_to_hall(all_rooms, hall):
    # print('move to hall', all_rooms, ' || ', hall)
    # Check the rooms
    for room_id, single_room in enumerate(all_rooms):

        # r is the index, and room will be tuple of two pods
        check_in_right_room = True
        for occupant in single_room:
            if check_in_right_room and occupant == room_id:  # If they match then cannot move
                check_in_right_room = True  # Don't break, check them all
            else:
                check_in_right_room = False

        if check_in_right_room:
            continue
        
        # could have replaced with  "if all(occupant == room_id for occupant in single_room):"
       
        for h_idx in range(len(hall)):
            cost = calculate_cost_to_move(single_room, hall, room_id, h_idx, into_room=False)

            if cost == INF:
                continue
            
            changed_room = all_rooms[:room_id] + (single_room[1:], ) + all_rooms[room_id + 1:]  # This empties the position in the room
            changed_hall = hall[:h_idx] + (single_room[0], ) + hall[h_idx + 1:]

            yield cost, (changed_room, changed_hall)


# Generates ALL valid move given rooms and hallway status. The functions all yield possible moves.
def possible_moves(rooms, hallway):
    yield from move_to_room(rooms, hallway)
    yield from move_to_hall(rooms, hallway)


def calculate_cost_to_move(room, hall, room_idx, hall_idx, into_room=False):

    # Need to calculate the start an end positions to then see if the hallway is clear.
    # NOTE: I could not get the math to work this out (was always out slightly).
    #       Have adapted to others code/formula and using a step map (tuples)

    # True / False == 1 / 0
    # print('costing:', room, hall, room_idx, hall_idx, into_room)
    
    
    ## need to print statement this to work out the maths!!1!


    ## if the room is less than the hall index then 
    if room_idx + 1 < hall_idx:
        start = room_idx + 2
        end = hall_idx + (not into_room)
    else:
        start = hall_idx + into_room
        end = room_idx + 2


    '''
    # "any" like writing "or" and "all" is like writing "and" over an iterable like a list
    # convieniece code to create checks with easier loops.  Replaces things like this
    # for element in some_iterable:
    #   if element:
    #       return True
    #   return False
    '''

    # If there are any positions in the hall that are not empty (None) then return INF(inity) as the cost i.e. cant move
    if any(pos is not None for pos in hall[start:end]):
        return INF

    # If moving to the room, the obj is in the hallway at spot h,
    # otherwise it's the first in the room.
    pod = hall[hall_idx] if into_room else room[0]

    # return 10 to the power of the pod id (0-3) multiplied by
    # the distance moved using the matrix (indexed by the two positions) + the space moved into the room (len will count how many already in room 0/1)
    return 10**pod * (ROOM_DISTANCE[room_idx][hall_idx] + (into_room + 2 - len(room)))


def check_room_target(rooms):

    for r, room in enumerate(rooms):
        # If not 2 pods in room, or ANY pod not in right room (based on 0-3) then not done
        if len(room) != 2 or any(pod != r for pod in room):
            return False
    
    # print('Found a solution')

    return True

@lru_cache(maxsize=None)
def compute_costs(all_rooms, hall):
    # print('compute costs: ',all_rooms,' || ', hall)

    if check_room_target(all_rooms):
        return 0

    best = INF

    for cost, next_state in possible_moves(all_rooms, hall):
        cost += compute_costs(*next_state)

        if cost < best:
            best = cost

    return best



def part1(data):
    """Solve part 1"""
    min_cost = compute_costs(data, hallway_spaces) 
                  
    return min_cost


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
    print("Tests")
    print(f'Test1.  Part1: {test_solution1} Part 2: {test_solution2}')


if __name__ == "__main__":    # print()

    runTest(input_test)

    solutions = solve(input)
    print('\nAOC')
    print(f"Solution 1: {str(solutions[0])} in {solutions[2][1]-solutions[2][0]:.4f}s")
    print(f"Solution 2: {str(solutions[1])} in {solutions[2][2]-solutions[2][1]:.4f}s")
    print(f"\nExecution total: {solutions[2][-1]-solutions[2][0]:.4f} seconds")