lines = open('input').read().strip().split('\n')

def getyx():
	for y, line in enumerate(lines):
		for x, val in enumerate(line):
			yield (y, x, val)
def add(src, delta):
	y, x = src
	dy, dx=src[0]-delta[0], src[1]-delta[1]
	while 0 <= y < y_max and 0 <= x < x_max:
		yield (y, x)
		y += dy
		x += dx
y_max = len(lines)
x_max = len(lines[0])
import collections
antennae = collections.defaultdict(list)
antinodes = set()
for y, x, val in getyx():
	if val != '.':
		antennae[val].append((y,x))

for type, nodes in antennae.items():
	for src in nodes:
		for delta in nodes:
			if src != delta:
				antinodes |= {*add(src, delta)}
print(len(antinodes))
