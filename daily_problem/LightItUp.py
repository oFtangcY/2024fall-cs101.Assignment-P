n, m = map(int, input().split())
a = [0] + list(map(int, input().split())) + [m]
tot = 0
ans = 0
s = 0

for i in range(1, n + 2, 2):
    tot += a[i] - a[i-1]

ans = tot
for i in range(2, n + 2, 2):
    s += a[i-1] - a[i-2]
    if a[i] > a[i-1] + 1:
        t = tot -s
        ans = max(ans, s + m - a[i-1] - t - 1)
print(ans)