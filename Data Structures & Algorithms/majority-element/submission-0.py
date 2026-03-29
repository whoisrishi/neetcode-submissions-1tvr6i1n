class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        counter = {}
        for item in  nums:
            counter[item] = counter.get(item,0) + 1
            if counter[item] > len(nums)//2:
                return item