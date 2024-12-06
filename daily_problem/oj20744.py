if __name__ == "__main__":
    val = list(map(int, input().split(',')))
    n = len(val)

    price, price_throw = val[0], val[0]
    ans = 0
    for i in range(1, n):
        price, price_throw = max(price + val[i], val[i]), max(price, price_throw + val[i])
        ans = max(ans, price_throw)

    print(ans)