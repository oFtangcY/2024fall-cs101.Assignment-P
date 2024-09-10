n = int(input())
ans = 0
recruit = 0
event = list(map(int, input().split()))
for i in range(n):
    if event[i] > 0:
        recruit += event[i]
    elif recruit > 0:
        recruit += event[i]
    else:
        ans += 1
print(ans)