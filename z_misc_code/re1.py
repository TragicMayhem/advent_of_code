
import re

print(re.findall(r'\d{1,5}','gfgfdAAA1234ZZZuijjk'))
m = re.match(r"(\w+) (\w+)", "Isaac Newton, physicist")
print(m.group(0))       # The entire match 'Isaac Newton'
print(m.group(1))       # The first parenthesized subgroup. 'Isaac'
print(m.group(2))       # The second parenthesized subgroup. 'Newton'
print(m.group(1, 2))    # Multiple arguments give us a tuple. ('Isaac', 'Newton')

print('\n Find numbers')

text = '1-3 a: abcde'
text2 = '1-34 a: abcde'
text3 = '17-19 a: abcde'

print(re.findall(r'\d{1,5}',text))
print(re.findall(r'\d{1,2}',text2))
print(re.findall(r'\d{1,2}',text3))
print(re.findall(r'(\d{1,2})-(\d{1,2}):',text3))

print('\n Find numbers separated by hypen')
chk = re.match(r"(\d+)-(\d+)", text)
print(chk.group(1, 2))

print('\n Find numbers separated by hypen and words')
chk = re.match(r"(\d+)-(\d+) ([a-z]): ([a-z]+)", text)
print(chk.group(1, 2, 3, 4))

print('\n Find all a')
print(re.findall('a', text))
print(len(re.findall('a', text)))
print(text.count('a'))

print('\n find bag txt pattern')
test_bags = '1 bright white bag, 2 muted yellow bags.'
print(re.sub(r'\Wbag[\,s\.]+',',',test_bags))

print('\n')

test_list = [  'ugknbfddgicrmopn','aaa','jchzalrnumimnmhp','haegwjzuvuyypxyu','dvszwmarrgswjxmb', 
'tthjguiikfme','kmdfnvuffjewllsnfgvgaapsnd']

#(\w)\1*
for x in test_list:
  out1a = re.match(r"(\w)\1", x)  
  out1b = re.findall(r"(\w)\1", x)  
  print(out1a, '\n', out1b)

print('\nOther re test')
test2_list = [  'qjhvhtzxzqqjkmpb','xxyxx','uurcxstgmygtbstg','ieodomkazucvgmuy']

# String 'qjhvhtzxzqqjkmpb'
# (\w)\1 - matches qq
# (\w)[a-z]\1 - matches hvh and zxz
# (\w{2}).*?\1 = matches qj qj
#     Full match	0-12	qjhvhtzxzqqj
#     Group 1.	0-2	qj

print(re.match(r"(\w)[a-z]\1", test2_list[0]))
for x in test2_list:
  print(x)
  out2a = re.findall(r"(\w)[a-z]\1", x) 
  out2b = re.findall(r"(\w{2}).*?\1", x) 
  print(out2a, '\n', out2b)

