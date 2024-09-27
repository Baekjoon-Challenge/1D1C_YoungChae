from sys import stdin
from itertools import permutations

N, M = map(int, stdin.readline().split())
arr = list(map(int, stdin.readline().split()))

combs = list(sorted(set(permutations(arr, M))))
for comb in combs:
    print(" ".join(map(str, comb)))

"""
4 4
1 1 2 2
"""