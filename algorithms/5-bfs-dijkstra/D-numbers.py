from collections import deque
n = 10000

a = int(input())
b = int(input())

used = [False] * n
prev = [-1] * n
res = []

d = deque()
d.append(a)
used[a] = True

while d:
    digit = d.popleft()

    if digit == b:
        break

    for u in range(4):
        if u == 0:
            if int(digit / 1000) != 9:
                v = digit + 1000
            else:
                v = digit

        elif u == 1:
            if digit % 10 != 1:
                v = digit - 1
            else:
                v = digit

        elif u == 2:
            v = int(str(digit % 1000) + str(int(digit / 1000)))

        elif u == 3:
            v = int(str(digit % 10) + str(int(digit / 10)))

        if not used[v]:
            used[v] = True
            d.append(v)
            prev[v] = digit

while (b != a):
    res.append(b)
    b = prev[b]

    if b == -1:
        break

res.append(a)

for v in reversed(res):
    print(v)
