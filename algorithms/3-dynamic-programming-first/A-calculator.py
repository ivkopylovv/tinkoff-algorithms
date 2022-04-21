n = int(input())
dp, path = [0] * 7 * (n + 1), [0] * 7 * (n + 1)

for i in range(n + 1):
    if dp[i * 3] == 0 or dp[i * 3] > dp[i]:
        dp[i * 3], path[i * 3] = dp[i] + 1, 3

    if dp[i * 2] == 0 or dp[i * 2] > dp[i]:
        dp[i * 2], path[i * 2] = dp[i // 2] + 1, 2

    if dp[i + 1] == 0 or dp[i + 1] > dp[i]:
        dp[i + 1], path[i + 1] = dp[i] + 1, 1

result = []

while(n > 1):
    if path[int(n)] == 1:
        result.append('1')
        n -= 1

    elif path[int(n)] == 2:
        result.append('2')
        n /= 2

    else:
        result.append('3')
        n /= 3

print(''.join(result[::-1]))
