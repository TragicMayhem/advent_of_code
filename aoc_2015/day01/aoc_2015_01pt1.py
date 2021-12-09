# https://adventofcode.com/2015/day/1

import pathlib

script_path = pathlib.Path(__file__).parent
input = script_path / 'input.txt'  
input_test = script_path / 'test.txt' 
 
 
file_in = input_test

with open(file_in, 'r') as file:
  lst = file.read()
  up = lst.count('(')
  down = lst.count(')')
  print(f'Up= { up } Down= { down } Final floor = { up-down } \n')
  