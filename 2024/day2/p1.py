li=open('example').readlines()

total = 0
for line in li:
  if not line.strip():
    break
  ln=[*map(int, line.split())]
  safe = (sorted(ln)==ln or sorted(ln,reverse=True)==ln) and all([1<=abs(i-j)<=3 for i, j in zip(ln, ln[1:])])
  total += safe
print(total)
