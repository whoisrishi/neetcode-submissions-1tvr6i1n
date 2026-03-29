class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        candidate = None
        counter = 0

        for el in nums:
            if counter == 0:
                candidate = el
                counter = 1
            elif el == candidate:
                counter += 1
            else:
                counter -= 1

        return candidate