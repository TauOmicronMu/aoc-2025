import itertools
import operator

from functools import reduce

lines = [] 
with open('../6.txt', 'r') as f:
	lines = [list(l.replace('\n', '')) for l in f.readlines()] 

cols = list(map(list, itertools.zip_longest(*lines, fillvalue=' ')))

splits = []
for i in range(len(cols)):
	if not all(x == ' ' for x in cols[i]):
		continue
	splits.append(i)	

problems = [] 
pos = 0
for split in splits:
	problems.append(cols[pos:split])
	pos = split + 1
problems.append(cols[pos:])

solutions = []
for p in problems:
	op = operator.mul if p[0][-1] == '*' else operator.add
	p[0][-1] = ' '
	
	vals = [int(''.join(v)) for v in p]

	solutions.append(reduce(op, vals))	
	

print(sum(solutions))
