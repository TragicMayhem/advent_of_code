#https://www.reddit.com/r/adventofcode/comments/3xflz8/comment/cy9uvmd
'''
import re

molecule = input.split('\n')[-1][::-1]
reps = {m[1][::-1]: m[0][::-1] 
        for m in re.findall(r'(\w+) => (\w+)', input)}
def rep(x):
    return reps[x.group()]

count = 0
while molecule != 'e':
    molecule = re.sub('|'.join(reps.keys()), rep, molecule, 1)
    count += 1

print(count)


No problem, I'll go line-by-line.

I didn't include the code to read the input, just assume you've read the file into the input variable.

molecule = input.split('\n')[-1][::-1]

This takes the input, splits it into a list with each line as an element and then takes the last one 
(which in this case is the last line or the molecule string) and reverses it. 
The [::-1] is a list slice shorthand for reversing (normally [start:end:step_size], but if you leave a 
spot blank, it assumes the beginning/end of the list).

reps = {m[1][::-1]: m[0][::-1] 
        for m in re.findall(r'(\w+) => (\w+)', input)}

This does a regex search on the input for someword1 => someword2. 
Since I used the capturing parens in the regex, re.findall returns 
a list of pairs that correspond to all of the matches. 
reps is a dict with the keys being each of the someword2s reversed corresponding to its someword1 
reversed in the regex match.

def rep(x):
    return reps[x.group()]

rep is a function that takes the result of a regular expression match and looks up the string that 
was matched in the reps dict (see re.match.group)

count = 0
while molecule != 'e':

Initialize count to 0 and loop as long as the molecule has not yet been reduced to the single electron.

molecule = re.sub('|'.join(reps.keys()), rep, molecule, 1)
count += 1

Replace the first match in molecule of any of the keys in reps ('|'.join(reps.keys()) will join 
each of the keys into one string separated by | characters; so '|'.join(['a', 'b', 'c']) == 'a|b|c'). 

re.sub can take a function as it's second argument instead of a replacement string. 

The regex match object is passed to the function, and whatever is returned will be replaced, 
in this case that would be the value corresponding to the key in reps that was matched.

Then just increment the count and continue until the string shrinks to 'e'
'''

import re
import pathlib

script_path = pathlib.Path(__file__).parent
input = script_path / 'input.txt'  # 576 / 

with open(input, 'r') as file:
    input=file.read()

    # This REVERSES (using [::-1]) the last element [-1] in the list
    molecule = input.split('\n')[-1][::-1]

    #   Now the molecule is reversed ALL THE REPLACEMENTS HAVE TO BE TO.
    # 
    #   re.findall(r'(\w+) => (\w+)', input)
    #   NOTES: This pattern matches the X ==> Y in the input data
    #          The (\w+) has brackets so will capture what it finds. Both parts in the MATCH object
    #   
    #   for m in re....
    #   NOTES: This is using list comprehension to loop through ALL the matched objects (m) in the re.findall above
    #
    #   m[1][::-1]: m[0][::-1] 
    #   NOTES: So the findall will capture TWO groups, returned in a match object that is a list. 
    #          0 is the first element, 1 is the secnod (and last)
    #          [::-1] - remember that reverses.  START:END:STEP so start to end and -1 steps (reverse)
    #          Using m[1] first means its taking the replacement (2nd grouping) and making that the key in the dict i.e. like a reverse look up.
    #
    #   { ... } around this all forms a dictionary, which is why its m[1]: m[0] - Key : Value


    replacements = {m[1][::-1]: m[0][::-1] 
            for m in re.findall(r'(\w+) => (\w+)', input)}
    
    print()
    print("Molecule:", molecule)
    print()
    print("Replacements:",replacements)
    

    # So this function will be used in the re.sub. It is passed a group object for ANY matches it finds from the pattern
    # In this case, it will be searching for all the replacement molecules chained together as or statements
    # Each one it finds (left most first) will be sent to the rep function
    # This function must return a string, if does this by taking the match, looking up in the replacements reverse dictionary and returning the 
    # target replacement
    # (perhaps needs some error handing to return x if no match found?)
    def rep(x):
        return replacements[x.group()]

    count = 0

    print("\nRegEx search string build from joining all the keys in the dictionary together (using or |):")
    print('|'.join(replacements.keys()))
    print()

    while molecule != 'e':
        # check = re.search('|'.join(replacements.keys()), molecule)
        molecule = re.sub('|'.join(replacements.keys()), rep, molecule, 1)
        count += 1

    print("Number of replacements to get to the target 'e':", count)