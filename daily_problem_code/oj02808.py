L, M = map(int, input().split())
tot = set(range(L + 1))
area = set()
for i in range(M):
    b, e = map(int, input().split())
    area.update(range(b, e + 1))
print(len(tot - area))
