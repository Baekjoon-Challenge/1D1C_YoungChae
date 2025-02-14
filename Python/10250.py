from sys import stdin

n = int(stdin.readline())
for i in range(n):
    H, W, N = map(int, stdin.readline().split(" "))
    if N % H == 0:
        print("%d%02d"%(H, N // H))
    else:
        print("%d%02d"%(N % H,  N // H + 1))