import math

N = int(input())
for i in range(math.floor(N / 6), 0, -1):
    if N % i == 0:
        print(i)
        break
