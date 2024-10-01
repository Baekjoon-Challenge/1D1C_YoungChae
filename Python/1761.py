from sys import stdin, setrecursionlimit
from collections import defaultdict
import math

setrecursionlimit(10**5) # 50,000

N = int(stdin.readline())
tree = [[] for i in range(N+1)]
weight = defaultdict(int)
height = [0] * (N+1) # 누적 합

for i in range(N-1):
    a, b, c = map(int, stdin.readline().split(' '))
    tree[a].append(b)
    tree[b].append(a)
    weight[(a, b)] = c
    weight[(b, a)] = c

M = int(stdin.readline())
q = [tuple(map(int, stdin.readline().split(' '))) for i in range(M)]

logn = int(math.log2(N)) + 1
parent = [[0] * logn for _ in range(N + 1)]
level = [0] * (N + 1)

def dfs(node, pnode):
    parent[node][0] = pnode
    level[node] = level[pnode] + 1
    height[node] = height[pnode] + weight[(pnode, node)]
    
    for child in tree[node]:
        if child != pnode:
            dfs(child, node)
            
dfs(1, 0)

# 이진 리프팅
for k in range(1, logn): # K제곱
    for node in range(1, N+1):
        parent[node][k] = parent[parent[node][k-1]][k-1]


def lca(a, b):
    if level[x] < level[y]:
        a, b = b, a # 5, 1
    
    for k in range(logn-1, -1, -1): # 큰수부터
        if level[a] - (1 << k) >= level[b]:
            a = parent[a][k]
    
    if a == b:
        return a
    
    for k in range(logn-1, -1, -1):
        if parent[a][k] != parent[b][k]:
            a = parent[a][k]
            b = parent[b][k]
    
    return parent[a][0]

# LCA
for x, y in q:
    print(height[x] + height[y] - 2 * height[lca(x, y)])
    