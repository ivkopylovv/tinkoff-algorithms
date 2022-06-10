def solve(s: str, n: int):
    z = [0] * n
    left, right = 0, 0

    for i in range(1, n):
        if right >= i:
            z[i] = min(z[i - left], right - i + 1)

        while i + z[i] < n and s[z[i]] == s[i + z[i]]:
            z[i] += 1

        if i + z[i] - 1 > right:
            left, right = i, i + z[i] - 1

    return z


n = int(input())
s = input()

res = solve(s + s[::-1], n * 2)

count = 0
index = n * 2 - 1

while(count != n):
    print(res[index], end=" ")
    count += 1
    index -= 1
