import math

def printMatrix(ans, n):
    for j in range(n):
        print(' '.join(map(str, ans[j])))

n, k = map(int, input().split())

if n**2 < k:
    print(-1)
    exit()

i = math.floor(n - math.sqrt(n**2 - k))
k -= (2*n - i)*i

ans = [[0 for _ in range(n)] for __ in range(n)]
for p in range(n):
    for q in range(i):
        ans[p][q], ans[q][p] = 1, 1

if k != 0:
    if k % 2 == 0:
        if n - i > 1:
            ans[i][i], ans[i + 1][i + 1] = 1, 1
            k -= 2
        for j in range(i + 1, i + 1 + k // 2):
            ans[i][j], ans[j][i] = 1, 1
    else:
        ans[i][i] = 1
        k -= 1
        for j in range(i + 1, i + 1 + k // 2):
            ans[i][j], ans[j][i] = 1, 1

printMatrix(ans, n)



