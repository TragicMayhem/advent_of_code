# https://adventofcode.com/2021/day/7

import pathlib
import time

script_path = pathlib.Path(__file__).parent
input_test = script_path / 'test.txt'  # 168
input = script_path / 'input.txt'  #  92881128

file_in = input #_test

# TIME TESTS
# input - using list of range and sum
# Least fuel: 92881128 Time 26.4 
# input - using n(n+1)/2
# Least fuel: 331067 Time 0.97 on ubuntu laptop / 2s on mac

answers = {}

if __name__ == "__main__":

  with open(file_in, 'r') as file:
    data=[[int(x) for x in row] for row in [line.split(',') for line in file]]
    data=data.pop()
    # print(data)

    t1 = time.perf_counter()

    min_pos=min(data)
    max_pos=max(data)

    for i in range(min_pos+1, max_pos+1):
      answers[str(i)] = 0

      for crabpos in data:
        # Slower version using range and lists
        # gap = list(range(1, abs(crabpos - i)+1))
        t=abs(crabpos - i)
        answers[str(i)] += (t*(t+1))/2
  
  # print(answers)
  print(f"Least fuel: {min(answers.values()):.0f}")
  print(f"Least fuel: {min(answers.values()):,.0f}")

  t2 = time.perf_counter()
  print(f"Execution: {t2-t1:.4f} seconds")