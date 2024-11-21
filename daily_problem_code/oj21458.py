def bag(items, T):
    dp = [0] + [-1]*(T + 1)
    maxt = 0
    for t_i, w_i in items:
        for t in range(T, t_i - 1, -1):
            if dp[t - t_i] != -1:
                dp[t] = max(dp[t], dp[t - t_i] + w_i)

    return dp[T]

if __name__ == '__main__':
    T, n = map(int, input().split())
    workingouts = []
    for _ in range(n):
        workingouts.append(tuple(map(int, input().split())))

    maxIncrease = bag(workingouts, T)
    print(maxIncrease)

