

"""
한줄에 1개의 퀸이 들어가야함으로. 
1개 줄에 첫번째무터 마지막까지 퀸을 놓아 본다.
다음 줄에 놓을때는 이전에 놓은 퀸의 위치로 놓을 수 있는 위치를 확인하고
놓을 수 있는 위치에만 놓는다.
a11111 i=0 
11b222 i=1 
121200 i=2   i=0 q=0 n=2, i=1 q=2 n=2
102120 i=3

"""
# 시간초과
N = int(input())
def dfs(queen):
    able = [True] * N
    n = len(queen)
    if n == N:
        return 1
    for i, q in enumerate(queen):
        able[q] = False # 세로같은줄 제거
        if 0 <= q+(n-i) < N: # 
            able[q+(n-i)] = False # (-1) 대각선 제거
        if 0 <= q-(n-i) < N:
            able[q-(n-i)] = False # (1) 대각선 제거
    cnt = 0
    for i, a in enumerate(able):
        if a == True:
            cnt += dfs(queen+[i])
    return cnt


print(dfs([]))
