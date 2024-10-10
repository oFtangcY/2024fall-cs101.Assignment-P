n, q = map(int, input().split())
ans = 0

relation = {}
for i in range(1, n + 1):
    for j in range(1, n + 1):
        relation[(i, j)] = 0

for _ in range(q):
    i ,j = map(int, input().split())
    relation[(i, j)] = 1

for i, j in relation.keys():
    if relation[(i, j)] == 1:
        for l in range(1, n + 1):
            if relation[(j, l)] == 1 and relation[(l, i)] == 1:
                ans = 1
                break

print(['No', 'Yes'][ans])