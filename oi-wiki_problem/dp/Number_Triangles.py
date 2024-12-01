r = int(input())
num_tri = []
dp = []
for i in range(1, r + 1):
    num_tri.append(list(map(int, input().split())))
    dp.append([-1 for _ in range(i)])

dp[-1] = num_tri[-1]

for j in range(r - 2, -1, -1):
    for k in range(j + 1):
        dp[j][k] = max(dp[j + 1][k], dp[j + 1][k + 1]) + num_tri[j][k]

print(dp[0][0])