a = list(map(int, input().split()))

max_el = max(a)
min_el = min(a)
length = max_el - min_el + 1
count = [0] * length
k = 0

for value in a:
    count[value - min_el] += 1

for i in range(length):
    for _ in range(count[i]):
        a[k] = i + min_el
        k += 1

print(*a)
