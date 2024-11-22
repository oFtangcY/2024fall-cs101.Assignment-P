n, l = map(int, input().split())
a = sorted(list(map(int, input().split())))
a.insert(0, -a[0])
a.append(2 * l - a[n])
b = [0] * (n + 1)

for i in range(n + 1):
    b[i] = a[i + 1] - a[i]

print('{:.9}'.format(0.5 * max(b)))