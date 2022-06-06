from collections import defaultdict
INF = 10 ** 9 + 7

n = int(input())
d, v = map(int, input().split())
r = int(input())
d -= 1
v -= 1

a = defaultdict(list)
used = [False] * n
start_vert = d
time = [INF] * n
time[d] = 0

for i in range(r):
    s, s_time, f, f_time = map(int, input().split())
    a[s - 1].append((s_time, f - 1, f_time))

while True:
    used[start_vert] = True
    min_time = INF

    for s_time, f, f_time in a[start_vert]:
        if s_time >= time[start_vert] and f_time < time[f]:
            time[f] = f_time

    for u in range(n):
        if not used[u] and time[u] < min_time:
            min_time = time[u]
            start_vert = u

    if min_time >= INF:
        print(-1) if time[v] == INF else print(time[v])
        exit()
