class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        i, j = 0, 0
        res = []

        # Alternate characters
        while i < len(word1) and j < len(word2):
            res.append(word1[i])
            res.append(word2[j])
            i += 1
            j += 1

        # Append remaining characters
        res.append(word1[i:])
        res.append(word2[j:])

        return "".join(res)