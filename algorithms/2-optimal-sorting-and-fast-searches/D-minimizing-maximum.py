def solve(x, y, l):
    left, right = -1, l

    while right - left > 1:

        mid = (right + left) // 2

        if x[mid] < y[mid]:
            left = mid
        else:
            right = mid

    if right == l or left >= 0 and max(x[left], y[left]) < max(x[right], y[right]):
        return left

    return right


n, m, l = map(int, input().split())
a = [list(map(int, input().split())) for i in range(n)]
b = [list(map(int, input().split())) for i in range(m)]
q = int(input())
result = []

for i in range(q):
    x, y = map(int, input().split())
    result.append(solve(a[x - 1], b[y - 1], l) + 1)

print(*result, sep='\n')
