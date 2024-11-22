n, q = map(int, input().split())
ans = 0

relation = {}
for i in range(1, n + 1):
    for j in range(i + 1, n + 1):
        relation[(i, j)] = 0

for _ in range(q):
    i ,j = map(int, input().split())
    relation[(min(i, j), max(i, j))] += 1
    if relation[(min(i, j), max(i, j))] == 2:
        ans = 1
        break

print(['No', 'Yes'][ans])
