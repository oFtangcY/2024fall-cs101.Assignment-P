n = int(input())
a = list(map(int, input().split()))
if sorted(a) == a:
    print('YES')
else:
    print('NO')
