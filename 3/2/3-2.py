banks = []
with open('../3.txt', 'r') as f: 
	banks  = [[int(n) for n in list(b.strip())] for b in f.readlines()]	

joltages = [] 
for bank in banks:
	batteries = [] 
	pos = 0
	for n in range(12, 0, -1):
		best = max(bank[pos:len(bank)-n+1])
		pos = bank.index(best, pos, len(bank)) + 1
		batteries.append(best)
	joltages.append(int(''.join([str(b) for b in batteries])))

print(sum(joltages))
