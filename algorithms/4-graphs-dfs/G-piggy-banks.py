from collections import defaultdict
import sys

sys.setrecursionlimit(100000)


def dfs(vert, a, used):
    used[vert] = 1
    global count

    for value in a[vert]:
        if not used[value]:
            dfs(value, a, used)

        elif used[value] == 1:
            count += 1

    used[vert] = 2


n = int(input())

count = 0
a = defaultdict(list)
used = [0] * n

for i in range(n):
    vert = int(input())
    a[vert - 1].append(i)

for i in range(n):
    if not used[i]:
        dfs(i, a, used)

print(count)
