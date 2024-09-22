import math

t = int(input())

for _ in range(t):
    n = int(input())
    ans = n * (n + 1) // 2 - 2 * (2 ** (math.log2(n) // 1 + 1) - 1)
    print(int(ans))
