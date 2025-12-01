lines=open('input').read().strip().split('\n')
eqns = []
import operator, itertools, collections

for line in lines:
	lft, right = line.split(':')
	lft = int(lft)
	eqns.append((lft, [*map(int, right.split())][::-1]))
total = 0
please_compile_this_pypy = lambda i,j: int(str(i)+str(j))
for eqn in eqns:
	result, source = eqn
	for ops in itertools.product([operator.mul, operator.add, please_compile_this_pypy], repeat=len(source)-1):
		source1 = source[:]
		for op in ops:
			top = source1.pop()
			over = source1.pop()
			source1.append(op(top, over))
		if source1 == [result]:
			total += result
			break
print(total)
