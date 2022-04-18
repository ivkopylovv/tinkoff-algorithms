def get_character(i):
    return chr(ord('a') + i)


size = 26
s = input()
weight = list(map(int, input().split()))

count = [0] * size

for c in s:
    count[ord(c) - ord('a')] += 1

chars = list(range(size))
chars.sort(key=lambda x: weight[x], reverse=True)

left, right = [], []

for c in chars:
    if count[c] > 1:
        left.append(get_character(c))
        right.append(get_character(c))
        count[c] -= 2

for c in range(size):
    while count[c] != 0:
        left.append(get_character(c))
        count[c] -= 1

right.reverse()

print(''.join(left + right))
