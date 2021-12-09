# https://adventofcode.com/2015/day/1

import pathlib

script_path = pathlib.Path(__file__).parent
input = script_path / 'input.txt'  
input_test = script_path / 'test.txt' 

 
file_in = input #_test

with open(file_in, 'r') as file:
  lst = file.read()

  for x in range(len(lst)):
    # Use string slicing to take string upto and including current position
    instructions_sofar = lst[:x+1]  
    
    up_sofar = instructions_sofar.count('(')
    down_sofar = instructions_sofar.count(')')

    # If more down than up then moving to the basement, so report and stop
    if down_sofar > up_sofar:
      print(f'\nPos x+1: {x + 1} Up  = { up_sofar } Down = { down_sofar } (Difference should be -1: {up_sofar-down_sofar }) \n')
      break
