ary=[*''.join(offset % 2 == 0 and chr(ord('0')+int(offset//2))*int(c) or '.' * int(c) for offset, c in enumerate(input().strip()))]

for offset, val in list(enumerate(ary))[::-1]:
	dot_offset = ary.index('.')
	if offset < dot_offset:
		break
	ary[offset], ary[dot_offset] = '.', val

print(sum(
	(ord(i)-ord('0'))*idx for idx, i in enumerate(ary) if i != '.'
))
