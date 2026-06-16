class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m, n = len(obstacleGrid), len(obstacleGrid[0])

        dp = [0] * n
        dp[-1] = 0 if obstacleGrid[m - 1][n - 1] else 1

        for r in range(m - 1, -1, -1):
            for c in range(n - 1, -1, -1):
                if obstacleGrid[r][c]:
                    dp[c] = 0
                elif c + 1 < n:
                    dp[c] += dp[c + 1]

        return dp[0]