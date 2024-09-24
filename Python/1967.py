from sys import stdin, setrecursionlimit
from collections import defaultdict
setrecursionlimit(10**6)

N = int(stdin.readline())
d = defaultdict(list)
for i in range(N-1):
    p, c, w = map(int, stdin.readline().split())
    d[p].append((c, w))

diameter = 0

def dfs(p):
    global diameter
    if len(d[p]) == 0:
        return 0
    cw = [dfs(c) + w for (c, w) in d[p]]
    diameter = max(sum(list(sorted(cw, reverse=True))[:2]), diameter)
    return max(cw)
        
dfs(1)
print(diameter)
