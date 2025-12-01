claws = open('input').read().strip().split('\n\n')
import re
def solve(ax, ay, bx, by, x, y):
	for token in range(400):
		for a in range(100):
			b = token - 3 * a
			if 0 <= b <= 100 and a * ax + b * bx == x and a * ay + b * by == y:
				return token
	return 0
total = 0
for claw in claws:
	a, b, prize = claw.split('\n')
	ax, ay = [int(match) for match in re.findall(r'(\d+)', a)]
	bx, by = [int(match) for match in re.findall(r'(\d+)', b)]
	x, y = [int(match) for match in re.findall(r'(\d+)', prize)]
	# a * ax + b * bx == x
	# a * ay + b * by == y
	tokens = solve(ax, ay, bx, by, x, y)
	total += tokens
print(total)
