class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = 0
        curr = 0
        prefix = {0:1}
        for n in nums:
            curr += n
            count += prefix.get(curr -k, 0)
            prefix[curr] = prefix.get(curr,0) +1
        return count