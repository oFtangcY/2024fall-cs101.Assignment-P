while True:
    n, p, m = map(int, input().split())
    if n == 0 and p == 0 and m == 0:
        break
    else:
        kids = list(range(1, n + 1))
        index = p - 1

        while len(kids) > 1:
            index = (index + m - 1) % len(kids)
            print(kids[index], end=',')
            kids.pop(index)

        print(kids[0])
