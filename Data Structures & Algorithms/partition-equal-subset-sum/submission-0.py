class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2:
            return False

        target = total // 2
        dp = {0}

        for num in nums:
            nxt = set(dp)
            for s in dp:
                if s + num == target:
                    return True
                if s + num < target:
                    nxt.add(s + num)
            dp = nxt

        return target in dp