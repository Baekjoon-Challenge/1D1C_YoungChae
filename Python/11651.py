print('\n'.join(list(map(lambda x: str(x[0])+" "+str(x[1]), list(sorted([list(map(int, input().split(' '))) for _ in range(int(input()))], key=lambda x: (x[1], x[0])))))))