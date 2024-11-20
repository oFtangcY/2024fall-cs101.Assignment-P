def chooseplayers(n, h_1, h_2):
    dp = [[0, 0, 0] for _ in range(n + 1)]

    for i in range(1, n + 1):
        dp[i][0] = max(dp[i - 1])
        dp[i][1] = max(dp[i - 1][0], dp[i - 1][2]) + h_1[i - 1]
        dp[i][2] = max(dp[i - 1][0], dp[i - 1][1]) + h_2[i - 1]

    return max(dp[n])

n = int(input())
h_1 = list(map(int, input().split()))
h_2 = list(map(int, input().split()))

ans = chooseplayers(n, h_1, h_2)
print(ans)