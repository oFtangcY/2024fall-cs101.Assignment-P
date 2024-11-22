n, m = map(int, input().split())
price = list(map(int, input().split()))
price.sort(reverse=False)
ans = []
for i in price:
    if i <= 0:
        ans.append(i)
if len(ans) >= m:
    profit = -sum(ans[:m])
else:
    profit = -sum(ans)
print(profit)