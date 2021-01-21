from pprint import pprint
import re

# https://adventofcode.com/2015/day/11

print("Advent of Code 2015 - Day 11 part 1 and 2")

# v1 - Seems brute force eern combinations  (fyi printing steps slows to death)

# Alternatives to implement:
# [x] - Initial check - look left to right, if its invalid char, then increment it, scrap rest to 'a' 
# [ ] - When increment if its invalid then skip it (and reset from that possition to 'a')

test_input = ['abcddffh',   # abcddffj
              'abcddfah',   # abcddfbb
              'abceefgh',   # abceefhh
              'abdeeghi',   # abdeffaa
              'abcdefgh',   # abcdffaa   From problem
              'ghijklmn']   # ghjaabcc   From problem << cant be aabaa 

puzzle_input_pt1 = 'hepxcrrq'   # hepxxyzz
puzzle_input_pt2 = 'hepxxyzz'   # heqaabcc

input_string = puzzle_input_pt2

invalid_letter = [ 'o', 'i', 'l']
alphabet = 'abcdefghijklmnopqrstuvwxyz'
group3char = list()

lower_char = ord('a')  # 97
upper_char = ord('z')  # 122


def inspect_pwd(pwd):
  '''
  Inspect password for invalid characters. 
  First one located, increment, and reset rest of chars to 'a'
  '''
  tmp_pwd_chars = list()
  for i in range(len(pwd)):
    
    if pwd[i] in invalid_letter:
      tmp_pwd_chars.append(chr(ord(pwd[i])+1))
      tmp_pwd_chars.append('a' * (len(pwd) - i - 1))
      break
    else:
      tmp_pwd_chars.append(pwd[i])
      
  new_pwd = "".join(tmp_pwd_chars)
  return new_pwd


def change_pwd(pwd):
  '''
  Take pwd, increment the last character (and loop until not increasing beyond 'z')
  '''
  chars = [ch for ch in pwd]
  i = len(chars) - 1 
  chars[i] = chr(ord(chars[i]) + 1) 
  # print('\n', chars[i], ord(chars[i]), ord('z'))
  
  while (ord(chars[i]) > ord('z')) and i >  0:
    # print(i, chars[i])
    chars[i] = 'a'
    i -= 1
    chars[i] = chr(ord(chars[i]) + 1) 

  new_pwd = "".join(chars)  
  return new_pwd


def pwd_valid(pwd):
  '''
  Take in string and check against conditions
  As soon as one fails return FAlse
  If passes each then final return is valid password (True)
  '''
  # print("\n-----\n     Checking:", pwd)

  # If list is empty then its invalid pwd
  check1 = [chars for chars in group3char if(chars in pwd)]
  if bool(check1) == False:   
    # print('\tcheck1',check1)
    return False

  # If anything in list then pwd is invalid
  check2 = [char for char in invalid_letter if(char in pwd)]
  if bool(check2) == True:  
    # print('\tcheck2',check2)
    return False

  # MIGHT FAIL IF THE PATTERNS THE SAME _ TO CHECK RULE
  # If the length is <2 then not got two pairs of double-chars
  check3 = re.findall(r"(([a-z])\2)", pwd)   # e.g. [('aa', 'a'), ('cc', 'c')]
  if len(check3) < 2:   
    # print('\tcheck3',len(check3), check3)
    return False

  return True


for i in range(len(alphabet)-2):
    combi = alphabet[i:i+3]
    check_invalid = [char for char in invalid_letter if(char in combi)]
    if not check_invalid:
      group3char.append(combi)

limit = len(input_string)
current_pwd = change_pwd(inspect_pwd(input_string))

while not pwd_valid(current_pwd):
  current_pwd = change_pwd(current_pwd)

print('Current pwd     :', input_string)
print('Next valid pwd  :', current_pwd)