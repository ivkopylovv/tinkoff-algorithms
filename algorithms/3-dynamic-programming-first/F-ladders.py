def solve(m, n):
    count = 0

    if n == 0:
        return 1

    for i in range(m + 1, n + 1):
        count += solve(i, n - i)

    return count


n = int(input())

print(solve(0, n))
