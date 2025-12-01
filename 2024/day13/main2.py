claws = open('input').read().strip().split('\n\n')
import re
def solve(p, q, r, s, x, y):
	if q*r == p*s:
		return 0
	a = (s*x - q*y)//(p*s - q*r)
	b = (r*x - p*y)//(q*r - p*s)
	if a * p + b * q == x and a * r + b * s == y:
		return 3*a + b
	return 0
total = 0
for claw in claws:
	a, b, prize = claw.split('\n')
	p, r = [int(match) for match in re.findall(r'(\d+)', a)]
	q, s = [int(match) for match in re.findall(r'(\d+)', b)]
	x, y = [int(match)+10000000000000 for match in re.findall(r'(\d+)', prize)]
	# a * p + b * q == x
	# a * r + b * s == y
	tokens = solve(p, q, r, s, x, y)
	total += tokens
print(total)
