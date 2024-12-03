class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        dp = [[False] * n for _ in range(n)]
        longest_str = s[0]
        maxlen = 1
        for i in range(n):
            dp[i][i] = True
            if i != n - 1 and s[i] == s[i + 1]:
                dp[i][i + 1] = True
                maxlen = 2
                longest_str = s[i] + s[i + 1]
    
        for i in range(n - 1, -1, -1):
            for j in range(i + 2, n):
                dp[i][j] = (dp[i + 1][j - 1] and s[i] == s[j])
                if dp[i][j] and maxlen < j - i + 1:
                    maxlen = j - i + 1
                    longest_str = s[i:j + 1]

        return longest_str
