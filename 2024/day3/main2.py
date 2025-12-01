import re
k=1
def foobar(i):
	global k
	if 'do()' in i:
		k=1;return 0
	elif 'don\'t()' in i:
		k=0;return 0
	else:
		a,b=map(int,i[:2]);return a*b*k
print(sum(map(foobar,re.findall(r'mul\(([0-9]+),([0-9]+)\)|(don\'t\(\))|(do\(\))',open('input').read()))))
