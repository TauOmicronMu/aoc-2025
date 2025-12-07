import itertools

lines = []
with open('../5-ex.txt', 'r') as f:
	lines = f.readlines() 

split_i = lines.index("\n")
ranges = sorted([tuple(map(int, r.strip().split('-'))) for r in lines[:split_i]],key=lambda k: k[0])

for i in range(len(ranges)):
	if i == len(ranges) - 1:
		break

	curr = ranges[i]
	next = ranges[i+1]
	if curr[1] >= next[0]:
		ranges[i+1]  = (curr[1]+1, next[1])

for range in ranges:
	print(range)

print(sum([e-s+1 for (s, e) in ranges]))

