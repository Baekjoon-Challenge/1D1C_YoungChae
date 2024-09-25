from sys import stdin, setrecursionlimit
from collections import defaultdict
setrecursionlimit(10**6)

V = int(stdin.readline())
d = defaultdict(list)

for i in range(V):
    line = list(map(int, stdin.readline().split()))
    if i == 0:
        root = line[0]
    for j in range(1, len(line)-1, 2):
        d[line[0]].append((line[j], line[j+1]))

diameter = 0

# 부모, 부모의부모 (역행방지)
def dfs(p, pp):
    global diameter, d
    cw = [dfs(c, p) + w for (c, w) in d[p] if c != pp]
    if len(cw) == 0:
        return 0
    diameter = max(sum(list(sorted(cw, reverse=True))[:2]), diameter)
    return max(cw)
        
dfs(root, 0)
print(diameter)

"""
8
6 5 1 7 1 -1
1 2 1 -1
2 1 1 3 1 -1
3 2 1 4 1 -1
4 3 1 5 1 8 2 -1
5 4 1 6 1 -1
7 6 1 -1
8 4 2 -1

"""