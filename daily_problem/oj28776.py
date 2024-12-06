from math import prod

n = int(input())
king_l, king_r = map(int, input().split())
l, r = [], []
max_pro = 0
for _ in range(n):
    a, b = map(int, input().split())
    max_pro = max(a * b, max_pro)
    l.append(a)
    r.append(b)

pro = prod(l + [king_l])
print(pro // max_pro)