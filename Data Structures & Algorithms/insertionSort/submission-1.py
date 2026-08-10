class Solution:
    def insertionSort(self, nums):
        if not nums:
            return []

        res = [nums.copy()]

        for i in range(1, len(nums)):
            j = i

            while j > 0 and nums[j].key < nums[j - 1].key:
                nums[j], nums[j - 1] = nums[j - 1], nums[j]
                j -= 1

            res.append(nums.copy())

        return res
