from collections import defaultdict
import sys

sys.setrecursionlimit(100000)


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


def dfs1(vert, a, used, result):
    used[vert] = True

    for value in a[vert]:
        if not used[value]:
            dfs1(value, a, used, result)

    result.append(vert + 1)


def topological_sort(a, n, result):
    used = [False] * n

    for i in range(n):
        if not used[i]:
            dfs1(i, a, used, result)


a = defaultdict(list)
result = []

with open('topsort.in', 'r') as f:
    n, m = map(int, f.readline().split())
    for i in range(m):
        u, v = map(int, f.readline().split())
        a[u - 1].append(v - 1)

if find_cycle(a, n):
    with open('topsort.out', 'w') as f:
        print(-1, file=f)
else:
    topological_sort(a, n, result)
    with open('topsort.out', 'w') as f:
        print(*reversed(result), file=f)
