MOD = 1000000007

def dinner(k):
    dp = [1] * 100007
    for i in range(k, 100001):
        dp[i] = (dp[i - k] + dp[i - 1]) % MOD

    prefix = [0] * 100007
    prefix[0] = dp[0]
    for i in range(1, 100007):
        prefix[i] = (prefix[i - 1] + dp[i]) % MOD

    return dp, prefix

if __name__ == "__main__":
    t, k = map(int, input().split())
    dp, prefix = dinner(k)
    
    for _ in range(t):
        a, b = map(int, input().split())
        if a == 0:
            print(prefix[b] % MOD)
        else:
            print((prefix[b] - prefix[a - 1]) % MOD)
