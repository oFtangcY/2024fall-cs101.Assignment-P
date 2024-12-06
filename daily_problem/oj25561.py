INF = float('inf')
tot_price = INF

def dfs(price: list, coupon: list, item, buy: list, m, n):
    global tot_price
    if item == n:
        buy_past_coupon = buy[:]
        for p in range(m):
            for q, x in coupon[p]:
                if buy[p] >= q:
                    buy_past_coupon[p] = min(buy_past_coupon[p], buy[p] - x)

        tot_price = min(tot_price, sum(buy_past_coupon) - 50 * (sum(buy) // 300))

        return

    for p in range(m):
        if price[item][p] == -1:
            continue

        buy[p] += price[item][p]
        dfs(price, coupon, item + 1, buy, m ,n)
        buy[p] -= price[item][p]


def main():
    n, m = map(int, input().split())
    price = [[-1] * m for _ in range(n)]
    for item in range(n):
        for si_i in input().split():
            si, i = map(int, si_i.split(':'))
            price[item][si - 1] = i

    coupon = [[] for _ in range(m)]
    for i in range(m):
        for q_x in input().split():
            q, x = map(int, q_x.split('-'))
            coupon[i].append((q, x))

    buy = [0] * m
    dfs(price, coupon, 0, buy, m, n)
    print(tot_price)

if __name__ == "__main__":
    main()