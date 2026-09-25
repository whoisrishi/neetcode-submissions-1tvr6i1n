class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        rank = {c: i for i, c in enumerate(order)}

        for i in range(len(words) - 1):
            a, b = words[i], words[i + 1]

            for j in range(min(len(a), len(b))):
                if rank[a[j]] < rank[b[j]]:
                    break
                if rank[a[j]] > rank[b[j]]:
                    return False
            else:
                if len(a) > len(b):
                    return False

        return True