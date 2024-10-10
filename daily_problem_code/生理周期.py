s = 0

while True:
    s += 1
    p, e, i, d = map(int, input().split())
    if p == -1 and e == -1 and i == -1 and d == -1:
        break
    p %= 23
    e %= 28
    i %= 33
    days_offset = (6 * p * 28 * 33 + 19 * e * 23 * 33 + 2 * i * 23 * 28 - d) % 21252
    if days_offset == 0:
        days_offset = 21252

    print('Case {}: the next triple peak occurs in {} days.'.format(s, days_offset))