from collections import defaultdict

n, m = map(int, input().split())

a = defaultdict(list)

for i in range(m):
    u, v = map(int, input().split())
    a[u - 1].append(v - 1)
    a[v - 1].append(u - 1)

visited = [False] * n
count = 0
temp = []
res = []

for vert in range(n):
    if visited[vert]:
        continue

    visited[vert] = True
    temp_queue = []
    temp_queue.append(vert)

    while temp_queue:
        vert = temp_queue.pop()
        temp.append(vert + 1)

        for to in a[vert]:
            if not visited[to]:
                visited[to] = True
                temp_queue.append(to)

    count += 1
    res.append(temp)
    temp = []

print(count)

for comp in res:
    print(len(comp))
    print(*sorted(comp))
