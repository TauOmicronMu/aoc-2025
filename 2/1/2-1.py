import re

ids = []
with open("../2-ex.txt", 'r') as f:  
	dat = f.readline().strip().split(',')
	for rng in dat:
		bounds = rng.split('-')
		ids += range(int(bounds[0]), int(bounds[1]))

invalid_ids = []
for s in ids:
	s = str(s)
	print(f"id: {s}")
	substrings = [s[i:j] for i in range(len(s)) for j in range(i + 1, len(s) + 1)] 
	print(f"substrings: {substrings}")

	for ss in substrings:
		if len(re.findall(f"{ss}", s)) > 1:
			print(f"substring was repeated: {ss}")
			invalid_ids.append(int(s)) 
			break 

print(sum(invalid_ids))
