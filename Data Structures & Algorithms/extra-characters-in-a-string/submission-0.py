class Solution:
    def minExtraChar(self, s: str, dictionary: list[str]) -> int:
        n = len(s)
        words = set(dictionary)
        dp = list(range(n + 1))

        for i in range(1, n + 1):
            dp[i] = dp[i - 1] + 1
            for j in range(i):
                if s[j:i] in words:
                    dp[i] = min(dp[i], dp[j])

        return dp[n]