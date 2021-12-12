PASSPORT_FIELDS = {
    'byr',
    'iyr',
    'eyr',
    'hgt',
    'hcl',
    'ecl',
    'pid',
    'cid'
}

REQUIRED_PP_FIELDS = PASSPORT_FIELDS.difference({'cid'})


# LINES FROM OTHER SCRIPTS

# grid = [((y,x),int(v)) for y, row in enumerate(open(filepath,'r').read().split('\n')) for x,v in enumerate(row)]
'''[((0, 0), 5),
 ((0, 1), 4),
 ((0, 2), 2),
 ((0, 3), 1),
 ((0, 4), 4),
 ((0, 5), 5),
 ((0, 6), 1),
 ((0, 7), 7),
'''