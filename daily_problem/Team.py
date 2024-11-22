n = int(input())
num = 0
att = [[] for i in range(n)]
for i in range(n):
    att[i] = list(map(int, input().split()))
    if sum(att[i]) >= 2:
        num += 1
print(num)