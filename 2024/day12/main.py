plots = open('input').read().strip().split('\n')
max_y = len(plots)
max_x = len(plots[0])

import collections

unexplored = [(y,x) for x in range(max_x) for y in range(max_y)]
regions = []

def explore(to_check, region, val):
	visited = set()
	while to_check:
		y, x = to_check.pop()
		for dy, dx in ((0, 1), (1, 0), (0, -1), (-1, 0)):
			n_y, n_x = y + dy, x + dx
			if 0 <= n_y < max_y and 0 <= n_x < max_x:
				if plots[n_y][n_x] == val:
					region.add((n_y, n_x))
					if (n_y, n_x) not in visited:
						to_check.append((n_y, n_x))
		visited.add((y, x))
	return region

while unexplored:
	y, x = point = unexplored.pop()
	region = explore(collections.deque([point]), {point}, plots[y][x])
	unexplored = [i for i in unexplored if i not in region]
	regions.append(region)

price = 0
for region in regions:
	area = len(region)
	perimeter = 0
	for y, x in region:
		for dy, dx in ((0, 1), (1, 0), (0, -1), (-1, 0)):
			n_y, n_x = y + dy, x + dx
			perimeter += not(0 <= n_y < max_y and 0 <= n_x < max_x) or plots[y][x] != plots[n_y][n_x]
	price += area * perimeter
print(price)
