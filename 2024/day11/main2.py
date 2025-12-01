stones = [*map(int, open('input').read().strip().split())]
import collections
totals = {val:stones.count(val) for val in stones}
def stonify(totals):
	newtotals = collections.defaultdict(int)
	for stone, count in totals.items():
		if stone == 0:
			newtotals[1] += count
		elif len(as_str:=str(stone)) % 2 == 0:
			half = len(as_str) // 2
			newtotals[int(as_str[:half])] += count
			newtotals[int(as_str[half:])] += count
		else:
			newtotals[stone * 2024] += count
	return newtotals

for i in range(75):
	totals = stonify(totals)
print(sum(count for count in totals.values()))
