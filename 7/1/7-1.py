state = []
with open('../7.txt', 'r') as f:
	state = [list(l.strip()) for l in f.readlines()]

starting_pos = state[0].index('S')
beam_indices = [starting_pos] 

splits = 0
for i in range(1, len(state)):
	step = state[i]
	hits = [(b, step[b]) for b in beam_indices]
	for (b, symb) in hits:
		if symb == '.':
			step[b] = "|" 
		elif symb == '^':
			step[b-1] = step[b+1] = "|"
			beam_indices.remove(b)
			beam_indices += [b-1, b+1]
			splits += 1

	beam_indices = list(set(beam_indices)) 	

for step in state:
	print(step)	

print(splits)
