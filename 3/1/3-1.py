banks = []
with open('../3.txt', 'r') as f: 
	banks  = [[int(n) for n in list(b.strip())] for b in f.readlines()]

joltages = [max([int(str(bank[i]) + str(max(bank[i+1:]))) for i in range(len(bank)-1)]) for bank in banks]

print(sum(joltages))
