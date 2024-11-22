t = int(input())
ans = []
for i in range(t):
    n = int(input())
    if n % 2 == 0:
        ans.append(n // 2 - 1)
    else:
        ans.append(n // 2)
for i in range(t):
    print(ans[i])