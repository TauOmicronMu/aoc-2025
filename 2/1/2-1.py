import re

ids = []
with open("../2.txt", 'r') as f:  
	dat = f.readline().strip().split(',')
	for rng in dat:
		bounds = rng.split('-')
		ids += range(int(bounds[0]), int(bounds[1])+1)

invalid_ids = [s for s in ids if re.fullmatch(r"(.+)\1", str(s)) is not None]

print(sum(invalid_ids))
