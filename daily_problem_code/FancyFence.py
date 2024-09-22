t = int(input())

for _ in range(t):
    n = int(input())
    if 360 % (180 - n) == 0:
        print('YES')
    else:
        print('NO')
