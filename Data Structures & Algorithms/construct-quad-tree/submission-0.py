class Solution:
    def construct(self, grid):
        def dfs(r, c, size):
            val = grid[r][c]
            same = True

            for i in range(r, r + size):
                for j in range(c, c + size):
                    if grid[i][j] != val:
                        same = False
                        break
                if not same:
                    break

            if same:
                return Node(val == 1, True)

            half = size // 2

            tl = dfs(r, c, half)
            tr = dfs(r, c + half, half)
            bl = dfs(r + half, c, half)
            br = dfs(r + half, c + half, half)

            node = Node(True, False)
            node.topLeft = tl
            node.topRight = tr
            node.bottomLeft = bl
            node.bottomRight = br

            return node

        return dfs(0, 0, len(grid))