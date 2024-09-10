n = int(input())
coin = list(map(int, input().split()))
coin.sort(reverse=True)
value = 0
for i in range(n + 1):
    if value <= 0.5 * sum(coin):
        value += coin[i]
    else:
        print(i)
        break