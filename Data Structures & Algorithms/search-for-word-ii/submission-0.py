class Solution:
    def findWords(self, board, words):
        trie = {}
        for word in words:
            node = trie
            for c in word:
                node = node.setdefault(c, {})
            node["$"] = word

        res = []
        rows, cols = len(board), len(board[0])

        def dfs(r, c, node):
            ch = board[r][c]
            if ch not in node:
                return

            node = node[ch]
            word = node.pop("$", None)
            if word:
                res.append(word)

            board[r][c] = "#"
            for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols and board[nr][nc] != "#":
                    dfs(nr, nc, node)
            board[r][c] = ch

        for r in range(rows):
            for c in range(cols):
                dfs(r, c, trie)

        return res