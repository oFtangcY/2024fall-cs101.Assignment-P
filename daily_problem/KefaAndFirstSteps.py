n = int(input())
a = list(map(int, input().split()))
len = 1
subsegment_len = []

for i in range(1, n):
    if a[i] >= a[i - 1]:
        len += 1
    else:
        subsegment_len.append(len)
        len = 1
subsegment_len.append(len)
print(max(subsegment_len))