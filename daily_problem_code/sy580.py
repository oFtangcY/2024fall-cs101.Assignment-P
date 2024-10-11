n, m = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(n)]
ans = 0

for i in range(n):
    for j in range(m):
        result = matrix[i][j] * (matrix[0][j] * 1000 + matrix[i][-1] * 100 + matrix[-1][j] * 10 + matrix[i][0])
        if result > ans:
            ans = result

print(ans)
