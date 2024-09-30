def match(a, b):
    pair = 0
    j_last = -1
    for i in range(len(a)):
        for j in range(j_last + 1, len(b)):
            if abs(b[j] - a[i]) <= 1:
                pair += 1
                j_last = j
                break
        if j_last == len(b) - 1:
            break
    print(pair)

n = int(input())
a = sorted(list(map(int, input().split())))
m = int(input())
b = sorted(list(map(int, input().split())))

match(a, b)