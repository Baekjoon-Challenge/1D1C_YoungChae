import sys

N = int(sys.stdin.readline())
line = list(map(int, sys.stdin.readline().split(" ")))

arr = list(sorted(line))

mid = 0 # 중간 좌표 탐색

for i in range(len(arr)):
    if arr[i] > 0:
        mid = i
        break

if arr[0] > 0: # 전부양수
    print(arr[0], arr[1])
elif arr[N-1] < 0: # 전부음수
    print(arr[N-2], arr[N-1])
else:
    p1 = 0 # 음수 측
    p2 = N-1 # 양수 측

    z_p1 = 0
    z_p2 = N-1

    while p1 < p2:
        if abs(arr[z_p1] + arr[z_p2]) > abs(arr[p1] + arr[p2]):
            z_p1, z_p2 = p1, p2

        if abs(arr[p1]) > abs(arr[p2]):
            p1 += 1
        elif abs(arr[p1]) < abs(arr[p2]):
            p2 -= 1
        else:
            z_p1 = p1
            z_p2 = p2
            break
    
    if z_p1 < z_p2:
        print(arr[z_p1], arr[z_p2])
    else:
        print(arr[z_p2], arr[z_p1])



"""
5
-99 -2 -1 4 98
"""

"""
-99 -2 -1 
98 4
"""