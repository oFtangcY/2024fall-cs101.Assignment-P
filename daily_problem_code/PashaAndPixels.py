def CheckSquare(tup):
    if field[tup[0] + 1][tup[1] + 1] == 1:
        if field[tup[0] + 1][tup[1]] == 1 and field[tup[0]][tup[1] + 1] == 1:
            return 1
    if field[tup[0] - 1][tup[1] + 1] == 1:
        if field[tup[0]][tup[1] + 1] == 1 and field[tup[0] - 1][tup[1]] == 1:
            return 1
    if field[tup[0] - 1][tup[1] - 1] == 1:
        if field[tup[0] - 1][tup[1]] == 1 and field[tup[0]][tup[1] - 1] == 1:
            return 1
    if field[tup[0] + 1][tup[1] - 1] == 1:
        if field[tup[0] + 1][tup[1]] == 1 and field[tup[0]][tup[1] - 1] == 1:
            return 1
    return 0

n, m, k = map(int, input().split())
field = [[[0] for i in range(m + 2)] for j in range(n + 2)]

for move in range(1, k + 1):
    pixel = tuple(map(int, input().split()))
    field[pixel[0]][pixel[1]] = 1

    if CheckSquare(pixel):
        print(move)
        break
else:
    print(0)