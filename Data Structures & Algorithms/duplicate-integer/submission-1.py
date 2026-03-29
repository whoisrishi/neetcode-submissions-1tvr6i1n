class Solution:
    def hasDuplicate(self, nums: list[int]) -> bool:
        return len(nums) != len(set(nums))