from sys import stdin, setrecursionlimit
import math

setrecursionlimit(10**5) # 50,000

N = int(stdin.readline())
tree = [[] for i in range(N+1)]
for i in range(N-1):
    a, b = map(int, stdin.readline().split(' '))
    tree[a].append(b)
    tree[b].append(a)

M = int(stdin.readline())
q = [tuple(map(int, stdin.readline().split(' '))) for i in range(M)]

logn = int(math.log2(N)) + 1
parent = [[0] * logn for _ in range(N + 1)]
level = [0] * (N + 1)

def dfs(node, pnode):
    parent[node][0] = pnode
    level[node] = level[pnode] + 1
    
    for child in tree[node]:
        if child != pnode:
            dfs(child, node)
            
dfs(1, 0)

# 이진 리프팅
for k in range(1, logn): # K제곱
    for node in range(1, N+1):
        parent[node][k] = parent[parent[node][k-1]][k-1]

# LCA
for x, y in q:
    if level[x] < level[y]:
        x, y = y, x # 5, 1
    
    for k in range(logn-1, -1, -1): # 큰수부터
        if level[x] - (1 << k) >= level[y]:
            x = parent[x][k]
    
    if x == y:
        print(x)
        continue
    
    for k in range(logn-1, -1, -1):
        if parent[x][k] != parent[y][k]:
            x = parent[x][k]
            y = parent[y][k]
    
    print(parent[x][0])