from sys import stdin
N = int(stdin.readline())
P = [int(stdin.readline()) for _ in range(N)]
DP = [1, 1, 1, 2, 2, 3, 4, 5, 7, 9]
for i in range(10, max(P)):
    DP.append(DP[i-1] + DP[i-5])
for p in P:
    print(DP[p-1])