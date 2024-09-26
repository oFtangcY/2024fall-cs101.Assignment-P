def LockorUnlock(x):
    if x == 0:
        return 1
    else:
        return 0

t = int(input())
for _ in range(t):
    n = int(input())
    ceil = [0 for _ in range(n)]
    for i in range(1, n + 1):
        for j in range(1, n // i + 1):
            ceil[i * j - 1] = LockorUnlock(ceil[i * j - 1])

    print(sum(ceil))