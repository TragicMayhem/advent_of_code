
import re

print(re.findall(r'\d{1,5}','gfgfdAAA1234ZZZuijjk'))
m = re.match(r"(\w+) (\w+)", "Isaac Newton, physicist")
print(m.group(0))       # The entire match 'Isaac Newton'
print(m.group(1))       # The first parenthesized subgroup. 'Isaac'
print(m.group(2))       # The second parenthesized subgroup. 'Newton'
print(m.group(1, 2))    # Multiple arguments give us a tuple. ('Isaac', 'Newton')

text = '1-3 a: abcde'
text2 = '1-34 a: abcde'
text3 = '17-19 a: abcde'

print(re.findall(r'\d{1,5}',text))
print(re.findall(r'\d{1,2}',text2))
print(re.findall(r'\d{1,2}',text3))
print(re.findall(r'(\d{1,2})-(\d{1,2}):',text3))

chk = re.match(r"(\d+)-(\d+)", text)
print(chk.group(1, 2))

chk = re.match(r"(\d+)-(\d+) ([a-z]): ([a-z]+)", text)
print(chk.group(1, 2, 3, 4))

print(re.findall('a', text))
print(len(re.findall('a', text)))
print(text.count('a'))
