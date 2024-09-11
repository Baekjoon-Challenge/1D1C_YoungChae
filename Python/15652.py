from itertools import combinations_with_replacement

N, M = map(int, input().split())

# 중복 조합
for p in combinations_with_replacement(range(1, N+1), M):
    print(' '.join(map(str, p)))