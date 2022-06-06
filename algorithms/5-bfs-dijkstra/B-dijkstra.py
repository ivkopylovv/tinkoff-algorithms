INF = 10 ** 9 + 7

with open('dijkstra.in', 'r') as file:
    n, s, f = map(int, file.readline().split())
    g = [r for r in file.readlines()]
    s -= 1
    f -= 1

d = [INF] * n
d[s] = 0
q = set(list(range(n)))

while q:
    node = min(q, key=lambda v: d[v])
    common_w = d[node]

    if common_w == INF or node == f:
        break

    q.remove(node)
    row = list(map(int, g[node].split()))

    for to in range(n):
        w = row[to]

        if w < 0:
            continue

        d[to] = min(d[to], common_w + w)

with open('dijkstra.out', 'w') as file:
    print(-1 if d[f] == INF else d[f], file=file)
