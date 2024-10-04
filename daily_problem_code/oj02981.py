a = list(map(int, input().split()))
b = list(map(int, input().split()))

sum = [0 for _ in range(len(a) + 1)]
sum[0] = (a[0] + b[0]) // 10
sum[-1] = (a[-1] + b[-1]) % 10

ans = 0

for i in range(len(a) - 1):
    sum[i + 1] = (a[i] + b[i]) % 10 + (a[i + 1] + b[i + 1]) // 10

for j in range(len(sum)):
    ans += sum[j] * (10**(len(sum) - 1 - j))

print(ans)
