class Solution:
    def maxSlidingWindow(self, nums, k):
        q = []
        l = 0
        res = []

        for r in range(len(nums)):
            while q and nums[q[-1]] < nums[r]:
                q.pop()

            q.append(r)

            if q[0] < l:
                q.pop(0)

            if r >= k - 1:
                res.append(nums[q[0]])
                l += 1

        return res