n = int(input())
force_tot = [0, 0, 0]
for _ in range(n):
    force = list(map(int, input().split()))
    force_tot = [a + b for a, b in zip(force, force_tot)]
if force_tot == [0, 0, 0]:
    print('YES')
else:
    print('NO')