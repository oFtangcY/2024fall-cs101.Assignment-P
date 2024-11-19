def maxCover(dp):
    dp.sort(keys=lambda x:x[1])
    cnt = 1
    ed = dp[0][1]

    for i in range(1, n):
        if dp[i][0] > ed:
            ed = dp[i][1]
            if ed != n:
                cnt += 1

    return cnt


t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))

    all = []
    dp = [[i, n] for i in range(n)]
    for i in range(n):
        suma = 0
        for j in range(i, n):
            suma += a[j]
            if suma == 0:
                dp[i][1] = j
                break

    print(maxCover(dp))
    