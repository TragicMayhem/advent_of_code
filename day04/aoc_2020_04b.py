import sys
import re

print("Advent of Code 2020 - Day 4 part 2")

dirpath = sys.path[0] + '\\'

# handle = open(dirpath + 'test.txt', 'r')
# handle = open(dirpath + 'test2.txt', 'r')
handle = open(dirpath + 'input.txt', 'r')

lines = handle.readlines()
handle.close()

eyecolour = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']

current = []
passports = []
valid_passport_count = 0


def check_hgt(data):
  ''' 
    If cm, the number must be at least 150 and at most 193.
    If in, the number must be at least 59 and at most 76.
  '''
  units = re.findall(r"(\d{2,3})(cm|in)", data)

  try:
    m, u = units[0]
  except:
    m = u = ''

  if u == 'in' and (59 <= int(m) <= 76): return True
  if u == 'cm' and (150 <= int(m) <= 193): return True 

  return False  # Catch all and return fale


def check_data(d):
  ''' 
    Check the validity of the data for each passport.
  '''
  # print(f'\n<<<<<< check_data(d) >>>>>>>\n{d}')
  byr_valid = 1920 <= int(d.get('byr', 0)) <= 2002
  iyr_valid = 2010 <= int(d.get('iyr', 0)) <= 2020
  eyr_valid = 2020 <= int(d.get('eyr', 0)) <= 2030
  ecl_valid = d.get('ecl', '') in eyecolour
  
  hcl_valid = True if re.match(r'#[0-9-a-f]{6}',d.get('hcl','')) else False
  pid_valid = True if re.match(r'^[0-9]{9}$',d.get('pid','')) else False
  
  hgt_valid = check_hgt(d.get('hgt',''))

  # This sets results to True if ALL the listed values are True. Could have just returned this but used for testing
  results = all([byr_valid, iyr_valid, eyr_valid, hcl_valid, ecl_valid, pid_valid, hgt_valid])

  # print("Test: [byr, iyr, eyr, hcl, ecl, pid, hgt]", [byr_valid, iyr_valid, eyr_valid, hcl_valid, ecl_valid, pid_valid, hgt_valid])
  
  return results


def turn_to_dict(pp):
  '''
  function to take in string
  use regular expression to find all the numbers
  store in an list then return as a dictionary
  '''
  parts = []
  for i in pp:
    parts.extend(re.findall(r"([a-z]{3}):([a-zA-Z0-9#]+)", i))
  return dict(parts)


data = [l.rstrip() for l in lines]

for line in data:
  current.extend(line.split(" "))
  if line == '':
    passports.append(turn_to_dict(current))
    current.clear()
else:
  passports.append(turn_to_dict(current))


for p in passports:
  # print(f"\n------\np:  {p}\np.keys:  {p.keys()}\nlen(keys):  {len(p.keys())}")
  # print(f"check(p.copy()):  {check_data(p.copy())}")
  # print(p, check_data(p.copy()))
  if len(p.keys()) == 8 or (len(p.keys()) ==7 and 'cid' not in p.keys()):
    if check_data(p.copy()):  # This checks data and will return True or False
      valid_passport_count += 1

print(f"\nTotal passports (correct keys): {len(passports)}")
print(f"Valid passports: {valid_passport_count} \n")