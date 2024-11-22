a = int(input())
if a%2 != 0:
    print(0,0)
else:
    n_max = int(a/2)
    if a%4 == 0:
        n_min = int(a/4)
    else:
        n_min = a//4 + 1
    print(int(n_min), int(n_max))
