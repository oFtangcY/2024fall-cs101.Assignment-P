def publicSeq(a, b):
    dp = [[0 for _ in range(len(b) + 1)] for __ in range(len(a) + 1)]

    for i in range(1, len(a) + 1):
        for j in range(1, len(b) + 1):
            if b[j - 1] == a[i - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i][j - 1], dp[i - 1][j])

    return dp[-1][-1]

if __name__ == '__main__':
    while True:
        try:
            a, b = input().split()
        except EOFError:
            break

        print(publicSeq(a, b))
