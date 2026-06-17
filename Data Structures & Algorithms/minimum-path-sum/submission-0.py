class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])

        dp = [float("inf")] * (cols + 1)
        dp[cols - 1] = 0

        for r in range(rows - 1, -1, -1):
            for c in range(cols - 1, -1, -1):
                dp[c] = grid[r][c] + min(dp[c], dp[c + 1])

        return dp[0]