from sys import stdin
print('\n'.join(list(map(lambda x: str(x[0]) + " " + x[1], sorted(list(map(lambda x: (int(x[0]), x[1]), [stdin.readline().strip().split(' ') for i in range(int(stdin.readline()))])), key=lambda x: x[0])))))

"""
3
21 Junkyu
21 Dohyun
20 Sunyoung
"""