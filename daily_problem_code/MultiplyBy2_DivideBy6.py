t = int(input())
for _ in range(t):
    n = int(input())
    i = 0
    j = 0
    while n % 3 == 0:
        n = n // 3
        i += 1
    while n % 2 == 0:
        n = n // 2
        j += 1
    if n > 1 or j > i:
        print(-1)
    else:
        print(2 * i - j)