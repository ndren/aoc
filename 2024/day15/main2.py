grid_data, move_data = open('input').read().strip().split('\n\n')
grid = [list(''.join(j=='#' and '##' or j == 'O' and '[]' or j=='.' and '..' or j=='@' and '@.' for j in i)) for i in grid_data.split('\n')]
moves = ''.join(move_data.split('\n'))
y_max = len(grid)
x_max = len(grid[0])
def get(location):
	y, x = location
	return grid[y][x]

def offset(src, direction, count):
	y, x = src
	dy, dx = direction
	return y + dy * count, x + dx * count
def movex(src, direction):
	delta = 0
	line = []
	while (ahead := get(offset(src, direction, delta))) not in '#.':
		delta += 1
		line.append(ahead)
	if ahead == '#':
		return False
	# ahead is .
	newline = ['.']+line
	for delta, value in enumerate(newline):
		y, x = offset(src, direction, delta)
		grid[y][x] = value
	return True

def movey(src, direction, visited):
	next_src = offset(src, direction, 1)
	y, x = src
	next_y, next_x = next_src
	ahead = get(next_src)
	dy = direction[0]
	if ahead == '#':
		return False
	if ahead == '.':
		return True
	result = True
	if ahead == '[':
		for recurse in ((y+dy, x+1), (y+dy, x)):
			if recurse not in visited:
				visited.add(recurse)
				result &= movey(recurse, direction, visited)
	if ahead == ']':
		for recurse in ((y+dy, x-1), (y+dy, x)):
			if recurse not in visited:
				visited.add(recurse)
				result &= movey(recurse, direction, visited)
	return result
def movey_real(src, direction, visited):
	next_src = offset(src, direction, 1)
	y, x = src
	next_y, next_x = next_src
	ahead = get(next_src)
	dy = direction[0]
	if ahead == '.':
		return
	if ahead == '[':
		for recurse in ((y+dy, x+1), (y+dy, x)):
			if recurse not in visited:
				visited.add(recurse)
				movey_real(recurse, direction, visited)

	if ahead == ']':
		for recurse in ((y+dy, x-1), (y+dy, x)):
			if recurse not in visited:
				visited.add(recurse)
				movey_real(recurse, direction, visited)
def movey_real_real(direction, visited):
	for src in sorted(visited, key=lambda pos: pos[0]*-direction[0]):
		next_src = offset(src, direction, 1)
		y, x = src
		next_y, next_x = next_src
		grid[next_y][next_x], grid[y][x] = grid[y][x], grid[next_y][next_x]
def nearest(y, x):
	best = 1e999
	for p in ((y,x), (y,x+1)):
		for edge in ((0,0),):
			s_y, s_x = p
			d_y, d_x = edge
			dy, dx = abs(s_y - d_y), abs(s_x - d_x)
			best = min(100*dy+dx, best)
	return best
lut = {
'^': (-1, 0),
'v': (1, 0),
'<': (0, -1),
'>': (0, 1),
}
robot = None
for y, row in enumerate(grid):
	for x, value in enumerate(row):
		if value == '@':
			robot = y, x
assert(robot)
for direction in moves:
	parsed_direction = lut[direction or input('give me yoru ')]
	y, x = parsed_direction
	if x:
		if movex(robot, parsed_direction):
			robot = offset(robot, parsed_direction, 1)

	if y:
		if movey(robot, parsed_direction, set()):
			visit = set()
			movey_real(robot, parsed_direction, visit)
			visit |= {robot}
			movey_real_real(parsed_direction, visit)
			robot = offset(robot, parsed_direction, 1)

total = 0
for y, row in enumerate(grid):
	for x, value in enumerate(row):
		if value == '[':
			total += nearest(y,x)
print(total)
