from sys import stdin
from collections import deque, defaultdict

T = int(stdin.readline())
case = []

for _ in range(T):
    N, K = map(int, stdin.readline().split(" "))

    delay = [0] + list(map(int, stdin.readline().split(" ")))
    edge = defaultdict(list)
    degree = [0] * (N + 1)

    for i in range(K):
        x, y = map(int, stdin.readline().split(" "))
        degree[y] += 1 # 진입 차수 증가
        edge[x].append(y)

    W = int(stdin.readline())

    # 지어야 하는 건물이 진입정점 0인경우 바로 완성 가능
    if degree[W] == 0:
        case.append(delay[W])
        continue

    queue = deque()
    cumulative_delay = [0] * (N + 1)

    for i in range(1, N + 1):
        if degree[i] == 0:
            queue.append(i)
            cumulative_delay[i] = delay[i]

    while queue:
        x = queue.popleft()

        if x == W:
            break

        # 종점의 차수와 현재 노드의 도착 차수가 같으면
        for y in edge[x]:
            degree[y] -= 1
            # 이때 cumulative delay는 optimize된 값으로 종료
            cumulative_delay[y] = max(cumulative_delay[y], delay[y] + cumulative_delay[x])

            if degree[y] == 0:
                queue.append(y)

    case.append(cumulative_delay[W])

for c in case:
    print(c)