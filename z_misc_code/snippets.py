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
