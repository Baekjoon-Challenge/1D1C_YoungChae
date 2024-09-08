from sys import stdin
N, M = map(int, stdin.readline().split())

arr = [True for _ in range(M-N+1)]
if N == 1:
    arr[0] = False

for i in range(max(N,2), M+1):
    for j in range(2, int(i**0.5)+1):
        if i % j == 0:
            arr[i-N] = False
            break

for i in range(N, M+1):
    if arr[i-N]:
        print(i)