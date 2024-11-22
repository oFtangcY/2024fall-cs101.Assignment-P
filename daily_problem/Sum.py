t = int(input())
for i in range(t):
    a, b, c = map(int, input().split())
    if 2 * max(a, b, c) == sum([a, b, c]):
        print('YES')
    else:
        print('NO')