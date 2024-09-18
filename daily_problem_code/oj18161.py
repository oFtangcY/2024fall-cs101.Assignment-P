matrix = [[], [], []]
r = [0, 0, 0]
c = [0, 0, 0]

for i in range(3):
    r[i], c[i] = map(int, input().split())
    for j in range(r[i]):
        matrix[i].append(list(map(int, input().split())))

if c[0] != r[1] or r[0] != r[2] or c[1] != c[2]:
    print('Error!')
else:
    multiply = [[0 for _ in range(c[1])] for __ in range(r[0])]
    for i in range(r[0]):
        for j in range(c[1]):
            for k in range(c[0]):
                multiply[i][j] += matrix[0][i][k] * matrix[1][k][j]
    for i in range(r[2]):
        for j in range(c[2]):
            print(multiply[i][j] + matrix[2][i][j], end=' ')
        print('\n', end='')
