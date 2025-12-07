state = []
with open('../7-ex.txt', 'r') as f:
	state = [list(l.strip()) for l in f.readlines()]

total = len(state)-1

starting_pos = state[0].index('S')
beam_indices = [starting_pos] 

for i in range(1, len(state)):
	print(f"----- ON STEP {i} OF {total} -----")
	step = state[i]
	hits = [(b, step[b]) for b in beam_indices]
	for (b, symb) in hits:
		hit_val = 1 if state[i-1][b] == 'S' else state[i-1][b]
		if symb == '.':
			step[b] = hit_val if step[b] == '.' else step[b] + 1 
		elif symb == '^':
			step[b-1] = hit_val if step[b-1] == '.' else step[b-1] + hit_val
			step[b+1] = hit_val if step[b+1] == '.' else step[b+1] + hit_val
			beam_indices.remove(b)
			beam_indices += [b-1, b+1]
			
	beam_indices = list(set(beam_indices))

	for step in state:
		print(step)
	print('\n')

symbs = ['.', '^']
print(sum([x for x in state[-1] if x not in symbs]))
