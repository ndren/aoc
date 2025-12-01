robots = open('input').read().strip().split('\n')
# 7847

# 7847 % 101 = 70
import re, collections, math
pos_vel = []
Y_MAX = 103
X_MAX = 101

def quadrant(x, y):
	if x == X_MAX // 2 or y == Y_MAX // 2:
		return None
	return (x < X_MAX // 2) + 2 * (y < Y_MAX // 2)

for robot in robots:
	match = re.match(r'p=(-?\d+),(-?\d+) v=(-?\d+),(-?\d+)', robot)
	assert match
	pos_vel.append([int(i) for i in match.groups()])
last_jmp = 1
seconds = 0
while 1:
	pos_final = []
	arry = [[' ' for x in range(X_MAX)] for y in range(Y_MAX)]
	for x, y, dx, dy in pos_vel:
		x_final = (x + seconds * dx) % X_MAX
		y_final = (y + seconds * dy) % Y_MAX
		pos_final.append((x_final, y_final))
	for x_final, y_final in pos_final:
		arry[y_final][x_final] = 'X'
	print('\n'.join(''.join(line) for line in arry))
	print(seconds)
	jump = input('Jump? ')
	last_jmp = jump.lstrip('-').isnumeric() and int(jump) or last_jmp
	seconds += last_jmp
