def solve1(s: str, n: int):
    z = [0] * n
    left, right = -1, -1

    for i in range(0, n - 1):
        if right > i:
            z[i] = min(z[left + right - i - 1], right - i)

        while i - z[i] >= 0 and i + z[i] + 1 < n and s[i - z[i]] == s[i + z[i] + 1]:
            z[i] += 1

        if i + z[i] > right:
            left, right = i - z[i] + 1, i + z[i]

    return z


def solve2(s: str, n: int):
    z = [1] * n
    left, right = 0, 0

    for i in range(1, n):
        if right > i:
            z[i] = min(z[left + right - i], right - i + 1)

        while i - z[i] >= 0 and i + z[i] < n and s[i - z[i]] == s[i + z[i]]:
            z[i] += 1

        if i + z[i] - 1 > right:
            left, right = i - z[i] + 1, i + z[i] - 1

    return z


s = input()
n = len(s)

res1 = solve1(s, n)
res2 = solve2(s, n)

sum = 0

for i in range(n):
    sum += res1[i] + res2[i]

print(sum)
