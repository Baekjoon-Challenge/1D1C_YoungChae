from sys import stdin

A, B, C = map(int, stdin.readline().split())
def re(a, b, c):
    if b == 0:
        return 1
    v = re(a, int(b/2), c)
    if b%2 == 0:
        return pow(v, 2, c)
    else:
        return pow(v, 2, c) * a % c
    
print(re(A, B, C) % C)

# pow(a, b, c) 로 그냥해도 되긴 한다. (내부적으로 분할정복)