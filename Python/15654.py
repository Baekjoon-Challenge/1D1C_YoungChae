from sys import stdin
from itertools import permutations

N, M = map(int, stdin.readline().split())
arr = list(map(int, stdin.readline().split()))

combs = list(permutations(arr, M))
print('\n'.join([' '.join(map(str, k)) for k in sorted(combs)]))
