class Solution:
    def pacificAtlantic(self, heights):
        m, n = len(heights), len(heights[0])
        pacific = set()
        atlantic = set()

        def dfs(r, c, seen):
            if (r, c) in seen:
                return
            seen.add((r, c))

            for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                nr, nc = r + dr, c + dc
                if 0 <= nr < m and 0 <= nc < n and heights[nr][nc] >= heights[r][c]:
                    dfs(nr, nc, seen)

        for r in range(m):
            dfs(r, 0, pacific)
            dfs(r, n - 1, atlantic)

        for c in range(n):
            dfs(0, c, pacific)
            dfs(m - 1, c, atlantic)

        return [[r, c] for r in range(m) for c in range(n)
                if (r, c) in pacific and (r, c) in atlantic]