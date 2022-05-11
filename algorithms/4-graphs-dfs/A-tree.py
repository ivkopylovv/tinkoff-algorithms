n, m = map(int, input().split())

visited = [False] * n
used = [0] * n
prev = [-1] * n
a = [0] * n
start_vert = 0
cycle = False

for i in range(n):
    a[i] = [0] * n

for i in range(m):
    idx = input().split()
    a[int(idx[0]) - 1][int(idx[1]) - 1] = 1
    a[int(idx[1]) - 1][int(idx[0]) - 1] = 1


def dfs(vert):
    visited[vert] = True

    for j in range(n):
        if a[vert][j] == 1 and not visited[j]:
            idx = j
            dfs(idx)


def find_cycle(vert):
    used[vert] = 1

    for j in range(n):
        to = a[vert][j]

        if used[to] == 0:
            prev[to] = vert
            find_cycle(to)

        elif used[to] == 1 and to != prev[vert]:
            cycle = True

    used[vert] = 2


for i in range(n):
    find_cycle(i)

if cycle:
    print('NO')
    exit()

dfs(start_vert)

if False in visited or m != n - 1:
    print('NO')

else:
    print('YES')
