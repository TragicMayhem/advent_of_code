import sys
from pprint import pprint

# https://adventofcode.com/2015/day/7

print("Advent of Code 2015 - Day 7 part 2")

dirpath = sys.path[0] + '\\'

# Now, take the signal you got on wire a (46065), override wire b to that signal, and reset the other wires (including wire a). 
# What new signal is ultimately provided to wire a?
filename = 'input.txt'  # a = 46065 > b and run again. a = 14134


# Input pattern  
#    {change} -> {target wire}
# {change} can be 
#   {Number}                # 123 -> x
#   {wire/#} AND {wire/#}   # x AND y -> d      a & b
#   {wire/#} OR {wire/#}    # x OR y -> e       a | b
#   {wire} LSHIFT {Number}  # x LSHIFT 2 -> f   a << 2
#   {wire} RSHIFT {Number}  # y RSHIFT 2 -> g   a >> 2
#   NOT {wire}              # NOT y -> i        ~a

instructions = dict()

def convert_int(val):
  '''
    Check if can convert str to int, if not return the str (ref to another wire)
  '''
  try: 
    return int(val)
  except: 
    return val 


def complete_wire(name, wires = None):
  '''
  Take the name of wire and recursively workout the set value.
  '''
  # print("\n-----\nname:", name)
  if wires == None: wires = dict()
  if name in wires.keys(): return wires.get(name)
 
  values = instructions[name]

  if len(values) == 1:  # SET
    # print("<1>", values)
    tmp = convert_int(values[0])
    wires[name] = tmp if isinstance(tmp, int) else complete_wire(tmp, wires)
       
  elif len(values) == 2:  # NOT
    # print("<2>", values)
    tmp = convert_int(values[1])
    wires[name] = ~ tmp & 0xFFFF if isinstance(tmp, int) else ~ complete_wire(tmp, wires) & 0xFFFF

  elif len(values) == 3:  # AND, OR, LSHIFT, RSHIFT
    # print("<3>", values)
    left_op = convert_int(values[0])
    right_op = convert_int(values[2]) 

    if not isinstance(left_op, int):
      left_op = complete_wire(left_op, wires)

    if not isinstance(right_op, int):
      right_op = complete_wire(right_op, wires)
      
    if isinstance(left_op, int) and isinstance(right_op, int):
      if "AND" in values: wires[name] = left_op & right_op
      if "OR" in values: wires[name] = left_op | right_op
      if "LSHIFT" in values: wires[name] = left_op << right_op
      if "RSHIFT" in values: wires[name] = left_op >> right_op
  
  # print("END:", wires)

  return wires[name]


with open(dirpath + filename, 'r') as file:
  lst = file.read().split('\n')
  lst = [x.replace('->', '').split() for x in lst]  # Split on 'x' in each string ('1x2x3')

  for l in lst:
    instructions[l[-1]] = l[:-1]  # key is the last list item, value is the rest of the list
 

instructions['b'] = ['46065']
print(f'\nValue on "a" = ', complete_wire('a'))
