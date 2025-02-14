from sys import stdin
n = int(stdin.readline())
for i in range(n):
    S = stdin.readline().strip()
    total = 0
    cnt = 0
    for s in S:
        if(s == 'O'):
            cnt += 1
            total += cnt
        else:
            cnt = 0
    print(total)
    