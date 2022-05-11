import sys
sys.setrecursionlimit(100000)

n, m = map(int, input().split())

a = [0] * (n + 2)
for i in range(n + 2):
    a[i] = [0] * (m + 2)

comp = [0] * (n + 2)
for i in range(n + 2):
    comp[i] = [0] * (m + 2)

for i in range(1, n + 1):
    symb = list(input())
    for j in range(1, m + 1):
        if symb[j - 1] == '#':
            a[i][j] = 1


def dfs(i, j, n, m):
    if i == n + 1 or j == m + 1:
        return

    if a[i - 1][j] and not comp[i - 1][j]:
        comp[i - 1][j] = comp[i][j]
        dfs(i - 1, j, n, m)

    if a[i + 1][j] and not comp[i + 1][j]:
        comp[i + 1][j] = comp[i][j]
        dfs(i + 1, j, n, m)

    if a[i][j - 1] and not comp[i][j - 1]:
        comp[i][j - 1] = comp[i][j]
        dfs(i, j - 1, n, m)

    if a[i][j + 1] and not comp[i][j + 1]:
        comp[i][j + 1] = comp[i][j]
        dfs(i, j + 1, n, m)


count = 1

for i in range(1, n + 1):
    for j in range(1, m + 1):
        if a[i][j] and not comp[i][j]:
            comp[i][j] = count
            dfs(i, j, n + 1, m + 1)
            count += 1

print(count - 1)
