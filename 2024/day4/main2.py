lines =[i for i in  open('input').readlines() if i.strip()]

y_max=len(lines)
x_max=len(lines[0])
def get(src, offsets):
	word = ''
	for offset in offsets:
		dest_y, dest_x = src[0]+offset[0], src[1] + offset[1]
		line = lines[dest_y:dest_y+1]
		word += line and line[0][dest_x:dest_x+1] or ''
	return word.count('MAS') + word.count('SAM')
total = 0
for c_x in range(x_max):
	for c_y in range(y_max):
		d1 = [(0,0),(1,1),(2,2)]
		d2 = [(2,0),(1,1),(0,2)]
		total += get((c_y,c_x), d1) & get((c_y, c_x), d2)

print(total)
