def getZ(s: str, n: int):
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


def solve(z: list, n: int):
    for i in range(1, n):
        if n % i == 0 and z[i] == n - i:
            return n / i

    return 1


s = input()
n = len(s)

print(int(solve(getZ(s, n), n)))
