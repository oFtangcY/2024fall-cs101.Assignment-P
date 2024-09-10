n = int(input())
color = input()
num = 0
for i in range(1, n):
    if color[i - 1] == color[i]:
        num += 1
print(num)