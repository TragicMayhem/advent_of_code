from collections import defaultdict
import pprint

data = {
 'Bob' : {'item1':3, 'item2':8, 'item3':6},
 'Jim' : {'item1':6, 'item4':7},
 'Amy' : {'item1':6,'item2':5,'item3':9,'item4':2}
}

flipped = defaultdict(dict)
for key, val in data.items():
    for subkey, subval in val.items():
        flipped[subkey][key] = subval

pprint.pprint(dict(flipped))
print('=====')

s = [('yellow', 1), ('blue', 2), ('yellow', 3), ('blue', 4), ('red', 1)]

d = {}
for k, v in s:
    d.setdefault(k, []).append(v)

print(s)
print(sorted(d.items()))

s = 'mississippi'
d = defaultdict(int)
for k in s:
    d[k] += 1
print(s)
print(sorted(d.items()))