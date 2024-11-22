t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    zip_a_b = zip(a, b)
    sorted_zip = sorted(zip_a_b, reverse=True, key=lambda x: x[0])
    a, b = map(list, zip(*sorted_zip))
    j = 0
    sumt = 0

    for i in range(n):
        maxt = a[i]
        if sumt + b[i] <= maxt:
            sumt += b[i]
        else:
            break
    else:
        maxt = 0

    print(max(sumt, maxt))
