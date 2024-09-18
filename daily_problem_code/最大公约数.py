import math

result = []
while True:
    try:
        m, n = map(int, input().split())
    except ValueError:
        break
    except EOFError:
        break
    result.append(math.gcd(m, n))
for i in result:
    print(i)