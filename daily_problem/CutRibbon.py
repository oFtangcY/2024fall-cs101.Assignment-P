dp = [-4000]*4007

def cut(n, a, b, c):
    dp[a], dp[b], dp[c] = 1, 1, 1
    for l in range(1, n + 1):
        for ll in [a, b, c]:
            if l >= ll:
                dp[l] = max(dp[l - ll] + 1, dp[l])

    return dp[n]

n, a, b, c = map(int, input().split())
print(cut(n, a, b, c))