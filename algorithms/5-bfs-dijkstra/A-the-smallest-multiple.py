from collections import deque
from sys import stdin


def get_new_digit(a: int, b: int, c: int):
    return (a * 10 + int(b)) % c


def solve(a: str, b: int, digits: list):
    r = 0

    for c in a:
        r = get_new_digit(r, c, b)
        q = deque()
        q.append(r)
        used, to = [0] * b, [None] * b
        used[r] = 1

        while q:
            v = q.popleft()

            if v == 0:
                res = ' '

                while to[v]:
                    v, digit = to[v]
                    res += str(digit)

                return a + res[::-1]

            for digit in digits:
                u = get_new_digit(v, digit, b)

                if not used[u]:
                    used[u] = 1
                    to[u] = (v, digit)
                    q.append(u)

        return -1


input = stdin.readline
x, k = input().split()
k = int(k)
_ = input()
d = sorted(list(map(int, input().split())))

print(solve(x, k, d))
