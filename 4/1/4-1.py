import itertools

grid = []
with open('../4.txt', 'r') as f:
	grid = [list(l.strip()) for l in f.readlines()]

positions = list(itertools.product([-1, 0, 1], [-1, 0, 1]))
positions.remove((0,0)) 
def can_access(row, col, grid):
	valid_positions = [(i, j) for (i, j) in positions if row + i in range(0, len(grid)) and col + j in range(0, len(grid[0]))]
	return sum([1 for (i, j) in valid_positions if grid[row+i][col+j] == '@']) < 4

count = 0
for row in range(len(grid)):
	for col in range(len(grid[row])):
		if grid[row][col] == '@' and can_access(row, col, grid):
			count += 1
print(count)
