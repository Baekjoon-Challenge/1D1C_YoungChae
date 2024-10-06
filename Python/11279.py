from sys import stdin
import heapq

N = int(stdin.readline())
heap = []
for _ in range(N):
    x = int(stdin.readline())
    if x == 0:
        if heap:
            print(-heapq.heappop(heap)) # 최대힙이므로 음수로
        else:
            print(0)
    else:
        heapq.heappush(heap, -x)