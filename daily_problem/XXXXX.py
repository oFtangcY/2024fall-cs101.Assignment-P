def CheckSumOfArray(n, x, array):
    total_sum = sum(array)

    if total_sum % x != 0:
        return n

    left, right = 0, n - 1

    while left < n and array[left] % x == 0:
        left += 1

    while right >= 0 and array[right] % x == 0:
        right -= 1

    if left >= right:
        return -1

    return max(n - left - 1, right)

t = int(input())
for _ in range(t):
    n, x = map(int, input().split())
    a = list(map(int, input().split()))

    max_len = CheckSumOfArray(n, x, a)
    print(max_len)