from sys import stdin
from collections import deque

N, K = map(int, stdin.readline().split(" "))

q = deque([N])
dist = [100001] * 100001
dist[N] = 0

while q:
    point = q.popleft()
    
    if point == K:
        print(dist[point])
        break 
    
    if point + 1 <= 100000 and dist[point + 1] > dist[point] + 1:
        dist[point + 1] = dist[point] + 1
        q.append(point + 1)
    if point - 1 >= 0 and dist[point - 1] > dist[point] + 1:
        dist[point - 1] = dist[point] + 1
        q.append(point-1)
    if point * 2 <= 100000 and dist[point * 2] > dist[point]:
        dist[point * 2] = dist[point]
        q.append(point*2)