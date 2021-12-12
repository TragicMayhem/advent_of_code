import pprint

def flatten(d, parent_key='', sep='_'):
    items = []
    for k, v in d.items():
        new_key = parent_key + sep + k if parent_key else k
        if isinstance(v, dict):
            items.extend(flatten(v, new_key, sep=sep).items())
        else:
            items.append((new_key, v))
    return dict(items)


def flatten2(d):
    out = {}
    for key, val in d.items():
        if isinstance(val, dict):
            val = [val]
        if isinstance(val, list):
            for subdict in val:
                deeper = flatten2(subdict).items()
                out.update({key + '_' + key2: val2 for key2, val2 in deeper})
        else:
            out[key] = val
    return out


test_data = {'a': 1, 'c': {'a': 2, 'b': {'x': 5, 'y' : 10}}, 'd': [1, 2, 3]}
pprint.pprint(test_data)
print(flatten(test_data))

print('')

nested = {'a': 1, 'b': 2, 'c': {'c1': [{'c11': 1, 'c12': 2, 'c13': 3}, {'c21': 1, 'c22': 2, 'c23': 3}], 'd1': [{'d11': 1, 'd12': 2, 'd13': 3}, {'d21': 1, 'd22': 2, 'd23': 3}]}, 'x': 1, 'y': 2}
pprint.pprint(nested)
print(flatten2(nested))



