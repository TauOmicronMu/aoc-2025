import operator

from functools import reduce

problems = [] 
with open('../6.txt', 'r') as f:
	problems = list(zip(*[' '.join(line.split()).split(" ") for line in f.readlines()])) 

solutions = [reduce(operator.mul if p[-1] == '*' else operator.add , map(int, p[:-1])) for p in problems]
print(sum(solutions))
