n = int(input())
a = sorted(list(map(int, input().split())))

dp = [0] * (n + 1)
dp[1] = pow(10, 4)

for i in range(2, n + 1):
    dp[i] = min(dp[i - 1], dp[i - 2]) + a[i - 1] - a[i - 2]

print(dp[n])
