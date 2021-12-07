# https://adventofcode.com/2021/day/7

import pathlib

script_path = pathlib.Path(__file__).parent
input_test = script_path / 'test.txt'  
input = script_path / 'input.txt'  #  

file_in = input #_test

answers = {}

if __name__ == "__main__":

  with open(file_in, 'r') as file:
    data=[[int(x) for x in row] for row in [line.split(',') for line in file]]
    data=data.pop()
    print(data)

    min_pos=min(data)
    max_pos=max(data)

    for i in range(min_pos+1,max_pos+1):
      print(i)
      answers[str(i)] = 0
      for crabpos in data:
        crab_fuel = abs(crabpos - i)
        answers[str(i)] += crab_fuel

  print(answers)

  print("Least fuel:",min(answers.values()))
