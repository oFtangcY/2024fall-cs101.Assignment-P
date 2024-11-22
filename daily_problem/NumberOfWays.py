n = int(input())
arr = list(map(int, input().split()))

total_sum = sum(arr)

if total_sum % 3 != 0:
    print(0)
    exit()

part_sum = total_sum // 3

ways = 0
prefix_sum = 0
count_first_part = 0

for i in range(n - 1):
    prefix_sum += arr[i]

    if prefix_sum == 2 * part_sum and i >= 1:
        ways += count_first_part

    if prefix_sum == part_sum:
        count_first_part += 1

print(ways)


