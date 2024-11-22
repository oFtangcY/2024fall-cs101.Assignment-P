n, m = map(int, input().split())
i = 1
while i <= n + (i - 1) // m:
    i += 1
print(i - 1)