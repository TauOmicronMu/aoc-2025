from itertools import combinations

coords = []
with open('../9.txt', 'r') as f:
	coords = [list(map(int, l.replace('\n', '').split(','))) for l in f.readlines()]

print(max([(abs(x2 - x1)+1) * (abs(y2 - y1)+1) for (x1, y1), (x2, y2) in combinations(coords, 2)]))
