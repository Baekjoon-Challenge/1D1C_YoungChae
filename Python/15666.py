from sys import stdin
from itertools import combinations_with_replacement

N, M = map(int, stdin.readline().split())
arr = list(set(map(int, stdin.readline().split())))

combs = list(sorted(map(lambda x: list(sorted(x)), combinations_with_replacement(arr, M))))
for comb in combs:
    print(" ".join(map(str, comb)))