t = int(input())
for i in range(t):
    n = int(input())
    j = 0
    k = 0
    ans = ''
    while 10**j < n:
        j += 1
    for i in range(j, -1, -1):
        if n // (10**i) != 0:
            ans = ans + str(n - n % (10**i)) + ' '
            k += 1
        n = n % (10**i)
    print(k)
    print(ans)