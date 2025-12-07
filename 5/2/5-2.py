import itertools

lines = []
with open('../5.txt', 'r') as f:
	lines = f.readlines() 

split_i = lines.index("\n")
ranges = sorted([list(map(int, r.strip().split('-'))) for r in lines[:split_i]],key=lambda k: k[0])

new_ranges = []
new_ranges.append(ranges[0]) 
for i in range(len(ranges)):
	prev = new_ranges[-1]
	curr = ranges[i]
	
	if curr[0] <= prev[1]:
		prev[1] = max(prev[1], curr[1])
	else:	
		new_ranges.append(curr)

print(sum(e - s + 1 for (s, e) in new_ranges))
