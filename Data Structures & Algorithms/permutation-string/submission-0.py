class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        count1 = [0] * 26
        count2 = [0] * 26

        for i in range(len(s1)):
            count1[ord(s1[i]) - ord('a')] += 1
            count2[ord(s2[i]) - ord('a')] += 1

        matches = 0
        for i in range(26):
            if count1[i] == count2[i]:
                matches += 1

        left = 0
        for right in range(len(s1), len(s2)):
            if matches == 26:
                return True

            idx = ord(s2[right]) - ord('a')
            count2[idx] += 1
            if count1[idx] == count2[idx]:
                matches += 1
            elif count1[idx] + 1 == count2[idx]:
                matches -= 1

            idx = ord(s2[left]) - ord('a')
            count2[idx] -= 1
            if count1[idx] == count2[idx]:
                matches += 1
            elif count1[idx] - 1 == count2[idx]:
                matches -= 1

            left += 1

        return matches == 26