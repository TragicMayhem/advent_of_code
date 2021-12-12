#https://github.com/tomp/AOC-2016/blob/master/day3/day3.py

vals = list([row[0] for row in triples] + 
             [row[1] for row in triples] + 
             [row[2] for row in triples])
triples2 = zip(vals[0::3], vals[1::3], vals[2::3])
