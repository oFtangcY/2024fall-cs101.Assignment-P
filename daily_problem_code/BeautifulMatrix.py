r = 0
for i in range(5):
    c = list(map(int, input().split()))
    if sum(c) == 1:
        k = c
        r = i
for i in range(5):
    if k[i] == 1:
        print(abs(r - 2) + abs(i - 2))