lines = open('input').read().strip().split('\n')

def getyx():
	for y, line in enumerate(lines):
		for x, val in enumerate(line):
			yield (y, x, val)
def add(src, delta):
	return (2*src[0]-delta[0], 2*src[1]-delta[1])

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
			antinode_y, antinode_x = add(src, delta)
			if src != delta and 0 <= antinode_y < y_max and 0 <= antinode_x < x_max:
				antinodes |= {(antinode_y, antinode_x)}
print(len(antinodes))
