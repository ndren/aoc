grid_data, move_data = open('input').read().strip().split('\n\n')
grid = [list(i) for i in grid_data.split('\n')]
moves = ''.join(move_data.split('\n'))
def get(location):
	y, x = location
	return grid[y][x]

def offset(src, direction, count):
	y, x = src
	dy, dx = direction
	return y + dy * count, x + dx * count
def move(src, direction):
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
	parsed_direction = lut[direction]
	if move(robot, parsed_direction):
		robot = offset(robot, parsed_direction, 1)
	
total = 0
for y, row in enumerate(grid):
	for x, value in enumerate(row):
		if value == 'O':
			total += 100*y + x
print(total)
