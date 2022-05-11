from collections import defaultdict
import sys

sys.setrecursionlimit(100000)
count = 0


def dfs(a, n, vert, used):
    used[vert] = True
    global count

    for value in a[vert]:
        if not used[value]:
            print(vert + 1, value + 1)
            count += 1

            if count == n - 1:
                exit()

            dfs(a, n, value, used)


n, m = map(int, input().split())

a = defaultdict(list)

for i in range(m):
    u, v = map(int, input().split())
    a[u - 1].append(v - 1)
    a[v - 1].append(u - 1)

count = 0
used = [False] * n

for i in range(n):
    if not used[i]:
        dfs(a, n, i, used)
