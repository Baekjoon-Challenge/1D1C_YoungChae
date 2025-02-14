from sys import stdin
from collections import deque

def bfs():
    H, W = map(int, stdin.readline().split(" "))
    arr = [list(map(int, stdin.readline().strip())) for _ in range(H)]

    # visited [벽 부심 여부][y][x]
    visited = [[[False for i in range(W)] for j in range(H)] for _ in range(2)]

    queue = deque([[0, 0, 0, 1]]) # 시작칸도 카운팅
    visited[0][0][0] = True

    move = [[1, 0], [0, 1], [-1, 0], [0, -1]]

    while queue:
        y, x, breaked, dist = queue.popleft()

        if y == H - 1 and x == W - 1:
            return dist

        for [my, mx] in move:
            ty, tx = y + my, x + mx
            if 0 <= ty < H and 0 <= tx < W:
                if arr[ty][tx] == 0 and not visited[breaked][ty][tx]:
                    queue.append([ty, tx, breaked, dist + 1])
                    visited[breaked][ty][tx] = True
                elif arr[ty][tx] == 1 and breaked == 0 and not visited[1][ty][tx]:
                    queue.append([ty, tx, 1, dist + 1])
                    visited[1][ty][tx] = True
    return -1

print(bfs())