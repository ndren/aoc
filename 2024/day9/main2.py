ary=[*''.join(offset % 2 == 0 and chr(ord('0')+int(offset//2))*int(c) or '.' * int(c) for offset, c in enumerate(input()))]
for val in sorted({i for i in ary if i != '.'}, reverse=True):
	offsets = [offset for offset, offval in enumerate(ary) if offval == val]
	start, end = min(offsets), max(offsets)+1
	alt = ''.join(i if i=='.' else ' ' for i in ary)
	dotstart = alt.find('.'*(end-start))
	dotend = dotstart + end - start
	if dotstart != -1 and dotend <= start:
		ary[start:end], ary[dotstart:dotend] = ary[dotstart:dotend], ary[start:end]
print(sum(
	(ord(i)-ord('0'))*idx for idx, i in enumerate(ary) if i != '.'
))
