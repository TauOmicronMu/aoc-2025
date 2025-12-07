import itertools

lines = []
with open('../5.txt', 'r') as f:
	lines = f.readlines() 

split_i = lines.index("\n")
ranges = [r.strip() for r in lines[:split_i]] 
ingredients = [i.strip() for i in lines[split_i+1:]]

print(len(ingredients))

valid_ids = [] 
for r in ranges: 
	bounds = [int(b) for b in r.split('-')]
	valid_ids += list(range(bounds[0], bounds[1]+1))

print(len(valid_ids))

print(len([i for i in map(int, ingredients) if i in valid_ids]))
