from sys import stdin
from itertools import combinations

L, C = map(int, stdin.readline().split(" "))
arr = list(stdin.readline().strip().split(" "))

momo = ['a', 'e', 'i', 'o', 'u']
mo = list(sorted([m for m in arr if m in momo]))
ja = list(sorted([x for x in arr if x not in momo]))

arr = []
for i in range(1, L - 1): # 최소 한개의 모음과 두개의 자음
    for mo_comb in combinations(mo, i):
        for ja_comb in combinations(ja, L - i):
            arr.append("".join(sorted(mo_comb + ja_comb)))

print("\n".join(sorted(arr)))