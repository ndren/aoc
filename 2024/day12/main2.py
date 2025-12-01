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

def orthogonal(dy, dx):
	if dy:
		return ((0, 1), (0, -1))
	return ((1,0), (-1, 0))

def paint(edges):
	color = 0
	canvas = {}
	to_paint = collections.deque([list(edges)[0]])
	visited = set()
	while to_paint:
		edge = to_paint.pop()
		if edge not in canvas:
			color += 1
			canvas[edge] = color
		y, x, dy, dx = edge
		if edge not in visited:
			for o_dy, o_dx in orthogonal(dy, dx):
				line_art_edge = y+o_dy, x+o_dx, dy, dx
				if line_art_edge not in canvas and line_art_edge in edges:
					canvas[line_art_edge] = color
					to_paint.append(line_art_edge)
		visited.add(edge)
		if not to_paint:
			left_edges = list(set(edges)-set(visited))
			if left_edges:
				to_paint.append(left_edges[0])
	return canvas


while unexplored:
	y, x = point = unexplored.pop()
	region = explore(collections.deque([point]), {point}, plots[y][x])
	unexplored = [i for i in unexplored if i not in region]
	regions.append(region)

price = 0
for region in regions:
	area = len(region)
	edges = []
	for y, x in region:
		for dy, dx in ((0, 1), (1, 0), (0, -1), (-1, 0)):
			n_y, n_x = y + dy, x + dx
			if not(0 <= n_y < max_y and 0 <= n_x < max_x) or plots[y][x] != plots[n_y][n_x]:
				edges.append((y, x, dy, dx))
	canvas = paint(set(edges))
	perimeter = len(set(canvas.values()))
	price += area * perimeter
print(price)
