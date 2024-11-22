result = []

while True:
    n, m = map(int, input().split())
    if n == 0 and m == 0:
        break
    else:
        monkey = list(range(1, n + 1))
        index = 0

        while len(monkey) > 1:
            index = (index + m - 1) % len(monkey)
            monkey.pop(index)

        result.append(monkey[0])

for j in result:
    print(j)
