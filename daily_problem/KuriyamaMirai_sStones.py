def prefixSum(v):
    prefix_sum = [0] * (n + 1)
    for i in range(1, n + 1):
        prefix_sum[i] = prefix_sum[i - 1] + v[i - 1]

    return prefix_sum

n = int(input())
v = list(map(int, input().split()))
u = sorted(v)
prefix_sum = [prefixSum(v), prefixSum(u)]
m = int(input())

for _ in range(m):
    question, l, r = map(int, input().split())
    print(prefix_sum[question - 1][r] - prefix_sum[question - 1][l - 1])
