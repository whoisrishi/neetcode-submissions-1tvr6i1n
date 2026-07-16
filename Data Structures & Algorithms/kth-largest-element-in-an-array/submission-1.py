class Solution:
    def findKthLargest(self, nums, k):
        target = len(nums) - k
        l, r = 0, len(nums) - 1

        while l <= r:
            m = (l + r) // 2

            if nums[l] > nums[m]:
                nums[l], nums[m] = nums[m], nums[l]
            if nums[l] > nums[r]:
                nums[l], nums[r] = nums[r], nums[l]
            if nums[m] > nums[r]:
                nums[m], nums[r] = nums[r], nums[m]

            nums[m], nums[r] = nums[r], nums[m]
            pivot = nums[r]

            p = l
            for i in range(l, r):
                if nums[i] < pivot:
                    nums[p], nums[i] = nums[i], nums[p]
                    p += 1

            nums[p], nums[r] = nums[r], nums[p]

            if p == target:
                return nums[p]
            if p < target:
                l = p + 1
            else:
                r = p - 1