class Solution:
    def subsetXORSum(self, nums):
        def dfs(i, x):
            if i == len(nums):
                return x
            return dfs(i + 1, x) + dfs(i + 1, x ^ nums[i])
        return dfs(0, 0)