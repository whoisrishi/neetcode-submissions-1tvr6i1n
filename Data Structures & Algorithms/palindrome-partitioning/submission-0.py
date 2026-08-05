class Solution:
    def partition(self, s: str):
        n = len(s)
        dp = [[False] * n for _ in range(n)]

        for i in range(n - 1, -1, -1):
            for j in range(i, n):
                if s[i] == s[j] and (j - i <= 2 or dp[i + 1][j - 1]):
                    dp[i][j] = True

        res = []
        path = []

        def dfs(i):
            if i == n:
                res.append(path[:])
                return

            for j in range(i, n):
                if dp[i][j]:
                    path.append(s[i:j + 1])
                    dfs(j + 1)
                    path.pop()

        dfs(0)
        return res