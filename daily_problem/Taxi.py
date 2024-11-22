from collections import Counter

n = int(input())
s = Counter(list(map(int, input().split())))

taxi = s[4] + s[3] + (s[2] + 1) // 2

if s[3] + 2 * (s[2] % 2) < s[1]:
    taxi += (s[1] - s[3] - 2 * (s[2] % 2) + 3) // 4

print(taxi)