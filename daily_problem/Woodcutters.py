n = int(input())

x = []
h = []
for _ in range(n):
    x_i, h_i = map(int, input().split())
    x.append(x_i)
    h.append(h_i)

if n == 1:
    print(1)
    exit()

fallen_tree = 2
for i in range(1, n - 1):
    if x[i] - x[i - 1] > h[i]:
        fallen_tree += 1
    elif x[i + 1] - x[i] > h[i]:
        fallen_tree += 1
        x[i] += h[i]

print(fallen_tree)