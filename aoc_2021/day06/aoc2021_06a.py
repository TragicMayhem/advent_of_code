# https://adventofcode.com/2021/day/6

import pathlib

script_path = pathlib.Path(__file__).parent
input_test = script_path / 'test.txt'  
input = script_path / 'input.txt'  #  

file_in = input #_test


if __name__ == "__main__":

  with open(file_in, 'r') as file:
    data=[line.split() for line in file]
