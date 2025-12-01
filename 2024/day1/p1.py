left,right=[],[]
for line in open('input','r').readlines():
	if not line.strip():
		break
	l,r=map(int,line.split())
	left.append(l)
	right.append(r)
left=sorted(left)
right=sorted(right)

print(sum(abs(i-j) for i,j in zip(left, right)))
