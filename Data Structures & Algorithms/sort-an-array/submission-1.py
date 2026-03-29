class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        # array of size 0 or 1 is already sorted
        if len(nums) <= 1:
            return nums

        # Divide
        middle = len(nums) // 2
        left = nums[:middle]
        right = nums[middle:]
        
        # Recursively sort left and right halves
        sorted_left = self.sortArray(left)
        sorted_right = self.sortArray(right)
        
        # Merge the sorted halves
        return self._merge(sorted_left, sorted_right)
    
    def _merge(self, left: List[int], right: List[int]) -> List[int]:
        i = 0
        j = 0
        result = []
        
        # Compare elements from left and right arrays
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1
        
        # Append any remaining elements
        result.extend(left[i:])
        result.extend(right[j:])
        
        return result