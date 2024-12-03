N = int(input())
dp = [1] * (N + 1)

for i in range(2, N + 1):
    for j in range(1, i):
        dp[i] += dp[i - j]

print(dp[N])