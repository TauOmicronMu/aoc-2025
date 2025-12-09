import matplotlib.pyplot as plt

from itertools import combinations
from shapely.geometry import Polygon

coords = []
with open('../9.txt', 'r') as f:
	coords = [list(map(int, l.replace('\n', '').split(','))) for l in f.readlines()]

candidates = [((abs(x2 - x1)+1) * (abs(y2 - y1)+1), (x1, y1), (x2, y2)) for (x1, y1), (x2, y2) in combinations(coords, 2)]
candidates.sort(reverse=True)
bounding_box = Polygon(coords) 
for (d, (x1, y1), (x2, y2)) in candidates:
	cand_poly = Polygon([(x1, y1), (x1, y2), (x2, y2), (x2, y1)])
	if not bounding_box.contains(cand_poly):
		continue
	print(d) 
	break  
