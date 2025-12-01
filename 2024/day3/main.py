import re
print(sum(map(lambda i: int(i[0])*int(i[1]),re.findall(r'mul\(([0-9]+),([0-9]+)\)',open('input').read()))))
