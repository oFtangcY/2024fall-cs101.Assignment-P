n = int(input())
num = list(map(int, input().split()))
unit = 0
for i in range(3):
    if num[i] % 2 == 0:
        unit += 1
    else:
        unit -= 1
if unit >= 1:
    unit = 1
else:
    unit = 0
for i in range(n):
    if num[i] % 2 == unit:
        print(i + 1)