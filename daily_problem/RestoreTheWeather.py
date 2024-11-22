t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    t_day = list((a[i], i) for i in range(n))
    t_day.sort()
    b.sort()
    ans = [0 for j in range(n)]
    for i in range(n):
        ans[t_day[i][1]] = b[i]
    print(' '.join(str(i) for i in ans))