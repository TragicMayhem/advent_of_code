print("Advent of Code 2020 - Day 1 part 1")

# Input file is a list of numbers, one per line
# Two of them add to 2020, that pair multiply together to get the answer

count = 0
num_dict = {}
answers = []

#handle = open('test.txt', 'r')

handle = open('input.txt', 'r')
lines_list = handle.readlines()
handle.close()

for num in lines_list:
  num_key = num.rstrip()
  num_dict[num_key] = 2020 - int(num_key)

for k, v in num_dict.items():  
  if str(v) in num_dict:
    obj = {'num1': int(k), 'num2': int(v), 'ans': int(k) * int(v)}
    answers.append(obj)
    count += 1

if count != 2:
    print("Warning: More than one combination")

print('Answer: ', answers)
