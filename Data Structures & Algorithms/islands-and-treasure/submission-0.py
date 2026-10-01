class Solution:
    def islandsAndTreasure(self, grid):
        m, n = len(grid), len(grid[0])
        q = []

        for r in range(m):
            for c in range(n):
                if grid[r][c] == 0:
                    q.append((r, c))

        i = 0

        while i < len(q):
            r, c = q[i]
            i += 1

            for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                nr, nc = r + dr, c + dc

                if 0 <= nr < m and 0 <= nc < n and grid[nr][nc] == 2147483647:
                    grid[nr][nc] = grid[r][c] + 1
                    q.append((nr, nc))