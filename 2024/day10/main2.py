mountain = [[int(i) for i in line] for line in open('input').read().strip().split('\n')]
max_y = len(mountain)
max_x = len(mountain[0])
def jump(s_y, s_x, dy, dx):
	s_x += dx
	s_y += dy
	if 0 <= s_x < max_x and 0 <= s_y < max_y:
		return s_y, s_x
tracks = set()
def paths(o_y, o_x, c_y, c_x, val, log):
	if val == 9:
		tracks.add((o_y, o_x, c_y, c_x, log))
		return
	for dx, dy in ((0,1), (1,0), (0,-1), (-1,0)):
		if new := jump(c_y, c_x, dy, dx):
			n_y, n_x = new
			if mountain[n_y][n_x] == val + 1:
				paths(o_y, o_x, n_y, n_x, val + 1, log + (n_y, n_x))

for o_y, line in enumerate(mountain):
	for o_x, val in enumerate(line):
		if val == 0:
			paths(o_y, o_x, o_y, o_x, 0, (o_y, o_x))
print(len(tracks))
