def getCandy(candy_types):
    v, w = map(int, input().split())
    candy_types.append((v / w, v, w))

def arrangeCandy(w_max, candy_types):
    tot_price = 0
    for unit_v, v, w in sorted(candy_types, reverse=True):
        if w <= w_max:
            w_max -= w
            tot_price += v
        else:
            tot_price += v * w_max / w
            break
    return tot_price

n, w_max = map(int, input().split())

candy_types = []

for _ in range(n):
    getCandy(candy_types)

print('{:.1f}'.format(arrangeCandy(w_max, candy_types)))
