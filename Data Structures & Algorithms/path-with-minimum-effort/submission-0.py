class Solution:
    def minimumEffortPath(self, heights):
        rows, cols = len(heights), len(heights[0])
        dist = [[float("inf")] * cols for _ in range(rows)]
        dist[0][0] = 0
        heap = [(0, 0, 0)]

        while heap:
            effort, r, c = heapq.heappop(heap)

            if (r, c) == (rows - 1, cols - 1):
                return effort

            if effort > dist[r][c]:
                continue

            for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                nr, nc = r + dr, c + dc

                if 0 <= nr < rows and 0 <= nc < cols:
                    new_effort = max(
                        effort,
                        abs(heights[r][c] - heights[nr][nc])
                    )

                    if new_effort < dist[nr][nc]:
                        dist[nr][nc] = new_effort
                        heapq.heappush(heap, (new_effort, nr, nc))