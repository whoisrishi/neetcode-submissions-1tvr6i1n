class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        return nums + nums
        # or
        # length = len(nums)
        # ans = [0] * (2*length)
        # for index in range(0,length):
        #     ans[index]= nums[index]
        #     ans[index + length] = nums[index]
        # return ans
