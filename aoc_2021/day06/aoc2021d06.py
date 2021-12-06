# https://adventofcode.com/2021/day/6

import pathlib

script_path = pathlib.Path(__file__).parent
input_test = script_path / 'test.txt'  # 5934 for 80d   26984457539 for 256d
input = script_path / 'input.txt'  #  390011 for 80d   1746710169834 for 256d 

file_in = input #_test

def model_fish(intial_fish, model_days):
  '''
  Take in the initial list of fish and use dictionaries to count the number of fish for the model_days
  On day 0, new fish added (day 8) and that parent fish is rest to (dy 6)
  '''
  newfish=0
  dict_fish_days = {}
    
  for d_count in range(8):
    dict_fish_days[str(d_count)] = +intial_fish.count(d_count)

  for d in range(model_days):
    for k,v in dict_fish_days.items():
      if k == "0":
        newfish = v
      else:
        dict_fish_days[str(int(k)-1)] = v      
        
    dict_fish_days["6"] += newfish
    dict_fish_days["8"] = newfish

  return sum(dict_fish_days.values())


if __name__ == "__main__":

  with open(file_in, 'r') as file:
    data=[[int(x) for x in row] for row in [line.split(',') for line in file]]
    lanternfish=data[0]

  print("Part 1 -  80 days", model_fish(lanternfish, 80))
  print("Part 2 - 256 days", model_fish(lanternfish, 256))