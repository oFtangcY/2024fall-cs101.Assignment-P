from bisect import bisect_left

def maxDeSeq(h):
    h.reverse()
    arr = []

    for i in range(n):
        ind = bisect_left(arr, h[i])
        if ind == len(arr):
            arr.append(h[i])
        else:
            arr[ind] = h[i]

    return len(arr)

if __name__ == '__main__':
    n = int(input())
    h = list(map(int, input().split()))

    print(maxDeSeq(h))
