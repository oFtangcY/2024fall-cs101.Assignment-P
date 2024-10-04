from collections import Counter

input()

box = Counter(map(int, input().split()))

print(max(box.values()))