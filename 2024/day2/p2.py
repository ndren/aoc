li=open('example').readlines()

total = 0
for line in li:
  if not line.strip():
    break
  lin=[*map(int, line.split())]
  safe = 0
  for i in range(len(lin)+1):
    ln=lin[:i]+lin[i+1:]
    if i == len(lin):
      ln=lin
    safe |= (sorted(ln)==ln or sorted(ln,reverse=True)==ln) and all([1<=abs(i-j)<=3 for i, j in zip(ln, ln[1:])])
  total += safe
print(total)
