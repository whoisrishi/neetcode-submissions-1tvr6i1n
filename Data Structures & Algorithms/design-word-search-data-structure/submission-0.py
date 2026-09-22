class WordDictionary:

    def __init__(self):
        self.root = {}

    def addWord(self, word: str) -> None:
        cur = self.root
        for c in word:
            if c not in cur:
                cur[c] = {}
            cur = cur[c]
        cur["#"] = True

    def search(self, word: str) -> bool:
        def dfs(node, i):
            if i == len(word):
                return "#" in node

            c = word[i]

            if c != ".":
                if c not in node:
                    return False
                return dfs(node[c], i + 1)

            for nxt in node:
                if nxt != "#" and dfs(node[nxt], i + 1):
                    return True

            return False

        return dfs(self.root, 0)