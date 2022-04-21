
def solve(i, j):
    if i >= 0 and j >= 0 and i < n and j < m:

        if a[i][j] == -1:
            a[i][j] = solve(i - 2, j - 1) + solve(i - 2, j + 1) + \
                solve(i - 1, j - 2) + solve(i + 1, j - 2)
    else:
        return 0

    return a[i][j]


n, m = map(int, input().split())
a = [[-1] * m] * n
a[0][0] = 1

print(solve(n - 1, m - 1))
