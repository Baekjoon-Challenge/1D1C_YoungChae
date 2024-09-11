from sys import stdin
N = int(stdin.readline())
arr = [list(map(int, stdin.readline().strip().split(' '))) for i in range(N)]

def dac(row, col, n):
    if n == 1:
        if arr[row][col] == 1:
            return 0, 1
        else:
            return 1, 0
    
    W1, B1 = dac(row, col, int(n/2)) # 1
    W2, B2 = dac(row, int(n/2) + col, int(n/2)) # 2
    W3, B3 = dac(int(n/2) + row, col, int(n/2)) # 3
    W4, B4 = dac(int(n/2) + row, int(n/2) + col, int(n/2)) # 4

    W = W1 + W2 + W3 + W4
    B = B1 + B2 + B3 + B4
    
    if W == 0: # B만 있음
        return 0, 1
    elif B == 0: # W만 있음
        return 1, 0
    else:
        return W, B
        
W, B = dac(0, 0, N)
print(W)
print(B)
