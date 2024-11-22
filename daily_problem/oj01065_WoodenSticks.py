from bisect import bisect_left

def maxDeSeq(w):
    arr = []

    for i in range(n):
        ind = bisect_left(arr, w[i])
        if ind == len(arr):
            arr.append(w[i])
        else:
            arr[ind] = w[i]

    return len(arr)

if __name__ == '__main__':
    t = int(input())
    ans = []
    for _ in range(t):
        n = int(input())
        lw = list(map(int, input().split()))
        l_w = []
        for i in range(0, 2 * n, 2):
            l_w.append((lw[i], lw[i + 1]))
        l_w.sort(key=lambda x:(-x[0], -x[1]))
        l, w = map(list, zip(*l_w))

        ans.append(maxDeSeq(w))

    print('\n'.join(map(str, ans)))
    