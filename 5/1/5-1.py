import itertools

lines = []
with open('../5.txt', 'r') as f:
	lines = f.readlines() 

split_i = lines.index("\n")
ranges = [tuple(map(int, r.strip().split('-'))) for r in lines[:split_i]] 
ingredients = [int(i.strip()) for i in lines[split_i+1:]]

print(len(list(set([i for i in ingredients for r in ranges if i >= r[0] and i <= r[1]]))))
