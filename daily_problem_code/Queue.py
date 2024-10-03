n = int(input())
t = sorted(list(map(int, input().split())))
t_in_line = t[:]
ans = 0
time_wait = 0

for i in range(0, n):
    if t[i] >= time_wait:
        ans += 1
        time_wait += t[i]

print(ans)