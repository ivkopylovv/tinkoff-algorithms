from collections import defaultdict
import sys

sys.setrecursionlimit(100000)


def dfs(vert, colour, a, used):
    used[vert] = colour

    for value in a[vert]:
        if not used[value] and colour == 2 and not dfs(value, 1, a, used):
            return False

        elif not used[value] and not dfs(value, 2, a, used):
            return False

        elif used[value] == colour:
            return False

    return True


n, m = map(int, input().split())
a = defaultdict(list)
result = True
used = [0] * n
start_colour = 1

for i in range(m):
    u, v = map(int, input().split())
    a[u - 1].append(v - 1)
    a[v - 1].append(u - 1)

for i in range(n):
    if not used[i]:
        result = dfs(i, start_colour, a, used)
        if not result:
            print('NO')
            exit()

print('YES')
