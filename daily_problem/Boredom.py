from collections import Counter


def delete(count):
    M = 100001
    dp = [[0, 0] for _ in range(M + 1)]

    for i in range(1, M + 1):
        dp[i][0] = max(dp[i - 1][0], dp[i - 1][1])
        dp[i][1] = dp[i - 1][0] + count[i]*i

    return max(dp[M][0], dp[M][1])


n = int(input())
a = sorted(list(map(int, input().split())))
count = Counter(a)

print(delete(count))



