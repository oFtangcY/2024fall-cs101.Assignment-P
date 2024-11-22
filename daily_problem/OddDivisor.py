t = int(input())
for i in range(t):
    n = int(input())
    while n > 1:
        if n % 2 == 0:
            n = n // 2
            continue
        else:
            print('YES')
            break
    if n == 1:
        print('NO')