from sys import stdin

n = int(stdin.readline())
m = list(stdin.readline().strip().split(" "))
d = dict()

for i, v in enumerate(sorted(list(set(m)), reverse=True)):
    d[v] = i
    print(i, v)
    
for k in m:
    print(d[k], end=" ")