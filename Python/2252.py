from sys import stdin
from collections import deque

N, M = map(int, stdin.readline().split(' '))
graph = {i: [] for i in range(1, N+1)}
indegree = [0] * (N+1) # 진입 차수

for i in range(M):
    a, b = map(int, stdin.readline().split(' '))
    graph[a].append(b)
    graph[b].append(a)
    indegree[b] += 1
    
Q = deque([i for i in range(1, N+1) if indegree[i] == 0])
order = []

while Q:
    node = Q.popleft()
    order.append(node)
    
    for n in graph[node]:
        indegree[n] -= 1
        if indegree[n] == 0:
            Q.append(n)
        
print(' '.join(map(str, order)))