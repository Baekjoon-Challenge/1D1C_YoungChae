from sys import stdin

N, M = map(int, stdin.readline().split())
arr = [list(map(int, stdin.readline().split(' '))) for i in range(N)]
q = [list(map(int, stdin.readline().split(' '))) for i in range(M)]

DP = [[0] * (N + 1) for i in range(N + 1)]

for i in range(1, N + 1):
    for j in range(1, N + 1):
        DP[i][j] = DP[i - 1][j] + DP[i][j - 1] - DP[i - 1][j - 1] + arr[i - 1][j - 1]
        
# 행, 열 정의가 반대임.
for i in range(M):
    x1, y1, x2, y2 = q[i]
    print(DP[x2][y2] - DP[x1 - 1][y2] - DP[x2][y1 - 1] + DP[x1 - 1][y1 - 1])

"""
4 3
1 2 3 4
2 3 4 5
3 4 5 6
4 5 6 7
2 2 3 4
3 4 3 4
1 1 4 4
"""