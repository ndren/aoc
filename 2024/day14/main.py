robots = open('input').read().strip().split('\n')
import re, collections, math
pos_vel = []
Y_MAX = 103
X_MAX = 101
SECONDS = 100

def quadrant(x, y):
	if x == X_MAX // 2 or y == Y_MAX // 2:
		return None
	return (x < X_MAX // 2) + 2 * (y < Y_MAX // 2)

for robot in robots:
	match = re.match(r'p=(-?\d+),(-?\d+) v=(-?\d+),(-?\d+)', robot)
	assert match
	pos_vel.append([int(i) for i in match.groups()])

pos_final = []

for x, y, dx, dy in pos_vel:
	x_final = (x + SECONDS * dx) % X_MAX
	y_final = (y + SECONDS * dy) % Y_MAX
	pos_final.append((x_final, y_final))
quadrant_counts = collections.defaultdict(int)

for x_final, y_final in pos_final:
	if (q := quadrant(x_final, y_final)) is not None:
		quadrant_counts[q] += 1

print(math.prod(quadrant_counts.values()))

