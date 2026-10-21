
class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        left, right = max(nums), sum(nums)

        while left < right:
            mid = (left + right) // 2
            subarrays = 1
            curr_sum = 0

            for num in nums:
                if curr_sum + num > mid:
                    subarrays += 1
                    curr_sum = num
                else:
                    curr_sum += num

            if subarrays <= k:
                right = mid
            else:
                left = mid + 1

        return left
