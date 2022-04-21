def solve(dp, n, m):
    if n == 1 and m == 1:
        return 1, 1, 1

    max_column, max_row, max_length = 0, 0, 0

    for i in range(n):
        for j in range(m):
            if dp[i][j] > 0:
                dp[i][j] = min(dp[i - 1][j - 1], dp[i - 1]
                               [j], dp[i][j - 1]) + 1

            if dp[i][j] > max_length:
                max_length = dp[i][j]
                max_column, max_row = i - max_length + 1, j - max_length + 1

    if (max_column == -1):
        max_column = 0

    if (max_row == -1):
        max_row = 0

    return max_length, max_column + 1, max_row + 1


n, m = map(int, input().split())
a = [0] * n

for i in range(n):
    a[i] = list(map(int, input().split()))

size, x, y = solve(a, n, m)

print(size)
print(x, y)
