s = input()
m = int(input())

n = len(s)
prefix_count = [0] * n

for i in range(1, n):
    prefix_count[i] = prefix_count[i - 1]
    if (s[i - 1] == '.' and s[i] == '#') or (s[i - 1] == '#' and s[i] == '.'):
        prefix_count[i] += 1

for _ in range(m):
    l, r = map(int, input().split())
    result = prefix_count[r - 1] - prefix_count[l - 1]
    print((r - l) - result)
