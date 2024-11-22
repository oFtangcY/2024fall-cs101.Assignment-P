x = list(map(int, input().split()))
IndexSum = x.index(max(x))
for i in range(4):
    if i != IndexSum:
        print(x[IndexSum] - x[i], end=' ')