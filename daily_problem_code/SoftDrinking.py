n, k, l, c, d, p, nl, np = map(int, input().split())
toast1 = k * l // nl
toast2 = c * d
toast3 = p // np
ans = min(toast1, toast2, toast3) // n
print(ans)