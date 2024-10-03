from sys import stdin

a = dict()

N = int(stdin.readline())
for i in list(map(int, stdin.readline().split())):
    a[i] = 1
M = int(stdin.readline())
for i in list(map(int, stdin.readline().split())):
    print(a.get(i, 0))
