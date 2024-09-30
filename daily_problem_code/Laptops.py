n = int(input())
s = [[int(x) for x in input().split()] for _ in range(n)]
s.sort(reverse=True)

for i in s[1:]:
    if i[1] > s[0][1]:
        print('Happy Alex')
        break

    s[0][1] = i[1]
else:
    print('Poor Alex')
