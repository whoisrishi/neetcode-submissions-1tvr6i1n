class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        shortest_len = len(strs[0])
        for word in strs:
            if len(word) < shortest_len:
                shortest_len = len(word)
        for char_index in range(shortest_len):
            for word in strs:
                if word[char_index] != strs[0][char_index]:
                    return strs[0][:char_index]
        return strs[0][:shortest_len]