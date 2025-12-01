import sys
sys.setrecursionlimit(0xFFFF)
def tr(dx,dy):
	if dx==1:
		return (0,1)
	elif dx==-1:
		return (0,-1)
	elif dy==1:
		return (-1,0)
	elif dy==-1:
		return (1,0)
	assert(0)
def move1(x,y,dx,dy,history,mp):
        while 1:
                new_x,new_y=x+dx,y+dy
                if new_y >= len(mp) or new_y < 0:
                        return history
                if new_x >= len(mp[new_y]) or new_x < 0:
                        return history
                if mp[new_y][new_x] == '#':
                        dx,dy=tr(dx,dy)
                else:x+=dx;y+=dy;history|={(new_x,new_y)}

def move2(x,y,dx,dy,history,mp):
	while 1:
		new_x,new_y=x+dx,y+dy
		if new_y >= len(mp) or new_y < 0:
			return False
		if new_x >= len(mp[new_y]) or new_x < 0:
			return False
		if mp[new_y][new_x] == '#':
			dx,dy=tr(dx,dy)
		else:
			if (new_x,new_y,dx,dy) in history:
				return True
			x+=dx;y+=dy;history|={(new_x,new_y,dx,dy)}

data=open('input').read().strip()
mp=data.split('\n')
for offset, line in enumerate(mp):
	if '^' in line:
		x,y=line.index('^'),offset
historys=move1(x,y,0,-1,set(),mp)-{(x,y)}
total = 0
for history in historys:
	mp1 = mp[:]
	hx,hy = history
	mp1[hy] = mp1[hy][:hx] + '#' + mp1[hy][hx+1:]
	total += move2(x,y,0,-1,set(),mp1)
print(total)


