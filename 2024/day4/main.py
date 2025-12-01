lines =[i for i in  open('input').readlines() if i.strip()]

y_max=len(lines)
x_max=len(lines[0])
def get(src, offsets):
	word = ''
	for offset in offsets:
		dest_y, dest_x = src[0]+offset[0], src[1] + offset[1]
		line = lines[dest_y:dest_y+1]
		word += line and line[0][dest_x:dest_x+1] or ''
	return word.count('XMAS') + word.count('SAMX')
total = 0
for c_x in range(x_max):
	for c_y in range(y_max):
		hor = [(0,k) for k in range(4)]
		ver = [(k,0) for k in range(4)]
		diag1 = [(k,k) for k in range(4)]
		diag2 = [(k,-k) for k in range(4)]
		total += sum(get((c_y, c_x), slice) for slice in (hor, ver, diag1, diag2))

print(total)
