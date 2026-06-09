class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        lis = []

        for num in nums:
            l, r = 0, len(lis)

            while l < r:
                m = (l + r) // 2
                if lis[m] < num:
                    l = m + 1
                else:
                    r = m

            if l == len(lis):
                lis.append(num)
            else:
                lis[l] = num

        return len(lis)