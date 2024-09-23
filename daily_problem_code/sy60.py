a, b = map(int, input().split())
ans = []
result = []
counter = 0
for i in range(a, b + 1):
    if i == (i // 100)**3 + (i % 100 // 10)**3 + (i % 10)**3:
        result.append(str(i))
        counter += 1
if result != []:
    print(' '.join(result))

if counter == 0:
    print('NO')
