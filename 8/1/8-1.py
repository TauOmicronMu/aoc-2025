import itertools 
import math
import operator

from functools import reduce

import matplotlib.pyplot as plt
import networkx as nx

TOTAL_CONNS = 10

def sld(a, b): 
	return math.sqrt((b[0]-a[0])**2 + (b[1]-a[1])**2 + (b[2]-a[2])**2)

coords = [] 
with open('../8-ex.txt', 'r') as f:
	coords = [list(map(int, l.strip().split(','))) for l in f.readlines()]

distances = sorted([(sld(a, b), tuple(a), tuple(b)) for (a, b) in itertools.combinations(coords,2)])


def is_path(G, a, b): 
	cs = [c for c in nx.connected_components(G) if a in c and b in c]
	return len(cs) > 0

nodes = []
G = nx.Graph() 
num_selected = 0
while num_selected < TOTAL_CONNS:
	_, a, b = distances.pop(0)
	if a not in nodes:
		G.add_node(a)
		nodes.append(a)
	if b not in nodes:
		G.add_node(b)
		nodes.append(b)
	if not is_path(G, a, b):
		G.add_edge(a, b)
		num_selected += 1

print(reduce(operator.mul, [len(c) for c in list(sorted(nx.connected_components(G)))[:3]]))

nx.draw(G)
plt.show()
