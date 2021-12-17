import re
# .*x=(-?\d+)\.{2}(-?\d+), y=(-?\d+)\.{2}(-?\d+)
text = 'gfgfdAAA1234ZZZuijjk'

m = re.search('AAA(.+?)ZZZ', text)
if m:
    found = m.group(1)

import re

text = 'gfgfdAAA1234ZZZuijjk'

try:
    found = re.search('AAA(.+?)ZZZ', text).group(1)
except AttributeError:
    # AAA, ZZZ not found in the original string
    found = '' # apply your error handling

# found: 1234