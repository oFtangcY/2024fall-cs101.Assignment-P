import math


def cantor(arr, n):
    ans = 0
    for i in range(n):
        tmp = 0
        for j in range(i + 1, n):
            if arr[i] > arr[j]:
                tmp += 1

        ans += tmp*math.factorial(n - i - 1)

    return ans

def anticantor(ind, n):
    ans = [0]*n
    arr = list(range(1, n + 1))
    for i in range(n):
        ans[i] = arr[ind // math.factorial(n - i - 1)]
        arr.pop(ind // math.factorial(n - i - 1))
        ind %= math.factorial(n - i - 1)

    return ans


m = int(input())
for _ in range(m):
    n, k = map(int, input().split())
    arr = list(map(int, input().split()))

    ind = cantor(arr, n)
    arrk = anticantor((ind + k) % math.factorial(n), n)

    print(' '.join(map(str, arrk)))


