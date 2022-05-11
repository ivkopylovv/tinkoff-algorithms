from collections import defaultdict


def dfs(a, vert, used, prev):
    used[vert] = True
    prev[vert] = True

    for value in a[vert]:
        if (not used[value] and dfs(a, value, used, prev)) or prev[value]:
            return True

    prev[vert] = False
    return False


def find_cycle(a, n):
    used = [False] * n
    prev = [False] * n

    for i in range(n):
        if not used[i] and dfs(a, i, used, prev):
            return True
    return False


n, m = map(int, input().split())
a = defaultdict(list)

for i in range(m):
    u, v = map(int, input().split())
    a[u - 1].append(v - 1)

if find_cycle(a, n):
    print(1)
else:
    print(0)
