n = int(input())
x = sorted(list(map(int, input().split())))
q = int(input())

i = 0
j = 0
shop = {}
while j <= x[-1]:
    if j < x[i]:
        shop[j] = i
        j += 1
    else:
        i += 1
        if i == n:
            break

for _ in range(q):
    money = int(input())
    if money >= x[-1]:
        print(n)
    else:
        print(shop[money])
