import itertools 
import math
import operator

from functools import reduce

import matplotlib.pyplot as plt
import networkx as nx


def sld(a, b): 
	return math.sqrt((b[0]-a[0])**2 + (b[1]-a[1])**2 + (b[2]-a[2])**2)

coords = [] 
with open('../8.txt', 'r') as f:
	coords = [list(map(int, l.strip().split(','))) for l in f.readlines()]

distances = sorted([(sld(a, b), tuple(a), tuple(b)) for (a, b) in itertools.combinations(coords,2)])


def is_path(G, a, b): 
	cs = [c for c in nx.connected_components(G) if a in c and b in c]
	return len(cs) > 0

nodes = []
G = nx.Graph() 
last_mult = 0
while not len(nodes) == len(coords) or not nx.is_connected(G):
	_, a, b = distances.pop(0)
	if a not in nodes:
		G.add_node(a)
		nodes.append(a)
	if b not in nodes:
		G.add_node(b)
		nodes.append(b)
	G.add_edge(a, b)
	last_mult = a[0] * b[0]

print(last_mult)

nx.draw(G)
plt.show()
