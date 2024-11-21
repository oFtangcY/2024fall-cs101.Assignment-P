def budget(weight, coins):
    M = float('INF')
    ww = list(coins.keys())
    dp = [0] + [M]*max(weight, max(ww))
    for w in ww:
        dp[w] = coins[w]

    for i in range(weight + 1):
        for w in ww:
            if i < w:
                continue
            elif dp[i - w] == M:
                continue

            dp[i] = min(dp[i], dp[i - w] + coins[w])

    return dp[weight]


if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        e, f = map(int, input().split())
        w_tot = f - e
        n = int(input())
        coins = {}
        for __ in range(n):
            p, w = map(int, input().split())
            last_p = coins.get(w, p)
            coins[w] = min(p, last_p)

        minBudget = budget(w_tot, coins)
        if minBudget == float('INF'):
            print("This is impossible.")
        else:
            print(f"The minimum amount of money in the piggy-bank is {minBudget}.")