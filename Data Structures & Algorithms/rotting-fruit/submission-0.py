class Solution:
    def orangesRotting(self, grid):
        m, n = len(grid), len(grid[0])
        q = []
        fresh = 0

        for r in range(m):
            for c in range(n):
                if grid[r][c] == 2:
                    q.append((r, c))
                elif grid[r][c] == 1:
                    fresh += 1

        minutes = 0
        i = 0

        while i < len(q):
            size = len(q) - i

            for _ in range(size):
                r, c = q[i]
                i += 1

                for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                    nr, nc = r + dr, c + dc

                    if 0 <= nr < m and 0 <= nc < n and grid[nr][nc] == 1:
                        grid[nr][nc] = 2
                        fresh -= 1
                        q.append((nr, nc))

            if i < len(q):
                minutes += 1

        return minutes if fresh == 0 else -1