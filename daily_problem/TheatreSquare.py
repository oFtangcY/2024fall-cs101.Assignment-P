import math

n, m, a = map(int, input().split())
result = int(math.ceil(n / a) * math.ceil(m / a))
print(result)