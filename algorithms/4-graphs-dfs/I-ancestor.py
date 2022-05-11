from collections import defaultdict
import sys

sys.setrecursionlimit(100000)


def dfs(vert, a, used, first, second):
    global count
    used[vert] = True
    count += 1
    first[vert] = count

    for val in a[vert]:
        if not used[val]:
            dfs(val, a, used, first, second)

    count += 1
    second[vert] = count


n = int(input())
verts = [int(i) for i in input().split()]

a = defaultdict(list)
first = [0] * (n + 1)
second = [0] * (n + 1)
used = [False] * (n + 1)
root = 0

for i in range(n):
    if verts[i] == 0:
        root = i
    else:
        a[verts[i] - 1].append(i)


count = 0
dfs(root, a, used, first, second)

m = int(input())

for i in range(m):
    u, v = map(int, input().split())

    if first[u - 1] < first[v - 1] and second[v - 1] < second[u - 1]:
        print(1)
    else:
        print(0)
