import sys

# https://adventofcode.com/2016/day/1

print("Advent of Code 2016 - Day 1 part 2")

dirpath = sys.path[0] + '\\'

filename = 'test2.txt'  # 4
filename = 'input.txt'  #

directions = ['N', 'E', 'S', 'W']
visited_locations = []


def calc_route(from_loc, dir, val):
  pos_ns, pos_ew = from_loc
  # print(from_loc, dir, val)
  
  for p in range(val):
    if dir == 'N':  pos_ns += 1
    if dir == 'S':  pos_ns -= 1
    if dir == 'E':  pos_ew += 1
    if dir == 'W':  pos_ew -= 1

    # print(f'{(pos_ns, pos_ew)}')

    new_loc = (pos_ns, pos_ew)
        
    if new_loc in visited_locations:
      # print(f"Location already visited {new_loc}")
      return True, new_loc

    visited_locations.append(new_loc)

  return False, new_loc


with open(dirpath + filename, 'r') as file:
  data = file.read().split(', ')

  val_ns = val_ew = 0
  pos_ns = pos_ew = 0
  facing_ind = 0
  facing = directions[facing_ind]
  
  loc = (pos_ns, pos_ew)
  visited_locations = [loc]

  for i in data:
    move_val = int(i[1:])
    
    if i[0] == 'R': 
      facing_ind = (facing_ind + 1) if facing_ind <3 else 0
      
    if i[0] == 'L':
      facing_ind = (facing_ind - 1) if facing_ind > 0 else 3
      
    visted_already, loc = calc_route(loc, directions[facing_ind], move_val)

    if visted_already:
      print("Visited location", loc)
      break
    
    # print(visited_locations)
    # print(f'END {i}; {facing_ind}; {directions[facing_ind]} > {loc}\n')

val_ew =  loc[1] * -1 if loc[1] < 0 else loc[1]
val_ns =  loc[0] * -1 if loc[0] < 0 else loc[0]
print("")
print(f'N-S difference: {val_ns} and E-W difference: {val_ew} so distance is {val_ns + val_ew}\n')
 