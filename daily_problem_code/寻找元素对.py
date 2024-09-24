n = int(input())
a = list(map(int, input().split()))
k = int(input())

counter = 0

for a_i in a:
    if a_i < (k + 1) // 2:
        if k - a_i in a:
            counter += 1

print(counter)