class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        counts = {}
        max_freq = 0
        result = 0

        for right in range(len(s)):
            counts[s[right]] = counts.get(s[right], 0) + 1
            max_freq = max(max_freq, counts[s[right]])

            while (right - left + 1) - max_freq > k:
                counts[s[left]] -= 1
                left += 1
            result = max(result, right - left + 1)

        return result