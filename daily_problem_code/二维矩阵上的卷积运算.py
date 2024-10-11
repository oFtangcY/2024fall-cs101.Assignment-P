m, n, p, q = map(int, input().split())
origin_matrix = [list(map(int, input().split())) for _ in range(m)]
core = [list(map(int, input().split())) for _ in range(p)]
image_matrix = [[0 for _ in range(n - q + 1)] for _ in range(m - p + 1)]

for i in range(m - p + 1):
    for j in range(n - q + 1):
        for l in range(p):
            for s in range(q):
                image_matrix[i][j] += origin_matrix[i + l][j + s] * core[l][s]

for i in image_matrix:
    for j in i:
        print(j, end=' ')
    print()