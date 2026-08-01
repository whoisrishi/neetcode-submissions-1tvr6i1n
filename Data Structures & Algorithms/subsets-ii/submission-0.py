class Solution:
    def subsetsWithDup(self, nums):
        nums.sort()
        res = []
        subset = []

        def dfs(start):
            res.append(subset[:])
            for i in range(start, len(nums)):
                if i > start and nums[i] == nums[i - 1]:
                    continue
                subset.append(nums[i])
                dfs(i + 1)
                subset.pop()

        dfs(0)
        return res