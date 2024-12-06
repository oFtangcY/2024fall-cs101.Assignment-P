if __name__ == "__main__":
    a = list(map(int, input().split()))
    n = len(a)
    price_in = a[0]
    price_out = a[0]
    prefix = 0

    dp = [0 for _ in range(n)]
    for i in range(1, n):
        dp[i] = a[i] - price_in
        prefix = max(prefix, dp[i])
        if a[i] < price_in:
            price_in = a[i]

    print(prefix)