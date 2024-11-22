def prefixSum(mat):
    dp = [[0 for _ in range(n + 1)] for __ in range(n + 1)]
    dp[0][0] = mat[0][0]

    for i in range(1, n + 1):
        for j in range(1, n + 1):
            dp[i][j] = dp[i - 1][j] + dp[i][j - 1] - dp[i - 1][j - 1] + mat[i - 1][j - 1]

    return dp

def maxSubMat(dp):
    maxSum = -128
    for l in range(n + 1):
        for k in range(n + 1):
            for i in range(l, n + 1):
                for j in range(k, n + 1):
                    maxSum = max(maxSum, dp[i][j] - dp[i - l][j] - dp[i][j - k] + dp[i - l][j - k])

    return maxSum

if __name__ == '__main__':
    n = int(input())
    nums = []
    while len(nums) < n**2:
        nums.extend(list(map(int, input().split())))
    nums.append(0)

    mat = []
    for i in range(n):
        mat.append(nums[i * n:(i + 1) * n])

    prefixsum = prefixSum(mat)
    print(maxSubMat(prefixsum))
