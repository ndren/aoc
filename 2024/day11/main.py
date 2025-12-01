stones = map(int, open('input').read().strip().split())

def stonify(stones):
	for stone in stones:
		if stone == 0:
			yield 1
		elif len(as_str:=str(stone)) % 2 == 0:
			half = len(as_str) // 2
			yield int(as_str[:half])
			yield int(as_str[half:])
		else:
			yield stone * 2024

for i in range(25):
	stones = stonify(stones)
print(sum(1 for stone in stones))
