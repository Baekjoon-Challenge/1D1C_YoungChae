from sys import stdin

N, M = map(int, stdin.readline().split(' '))
arr = list(map(int, stdin.readline().split(' ')))

dp = [0] * (N+1)
for i in range(1, N+1):
    dp[i] = dp[i-1] + arr[i-1]   

for i in range(M):
    a, b = map(int, stdin.readline().split(' '))
    print(dp[b] - dp[a-1])

    