def get_prefix_function(s: str, n: int):
    p = [0] * n

    for i in range(1, n):
        cur = p[i - 1]

        while s[i] != s[cur] and cur > 0:
            cur = p[cur - 1]

        if s[i] == s[cur]:
            p[i] = cur + 1

    return p


def solve(pref: list, n: int, s_size: int):
    res = []

    for i in range(n):
        if pref[i] == s_size:
            res.append(i - s_size * 2)

    return res


text = input()
s = input()

text_size = len(text)
s_size = len(s)
n = text_size + s_size + 1

print(*solve(get_prefix_function(s + '#' + text, n), n, s_size))
