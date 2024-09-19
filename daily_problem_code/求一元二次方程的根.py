import math

n = int(input())
result = ''

for _ in range(n):
    a, b, c = map(float, input().split())
    y1 = -b / (2 * a)
    if y1 == 0:
        y1 = 0
    delta = b ** 2 - 4 * a * c
    if delta == 0:
        result += str('x1=x2={:.5f}\n'.format(y1))
    elif delta > 0:
        result += str('x1={:.5f};x2={:.5f}\n'.format(y1 + math.sqrt(delta) / (2 * a), y1 - math.sqrt(delta) / (2 * a)))
    else:
        result += str('x1={:.5f}+{:.5f}i;x2={:.5f}-{:.5f}i\n'.format(y1, math.sqrt(-delta) / (2 * a), y1, math.sqrt(-delta) / (2 * a)))

print(result)