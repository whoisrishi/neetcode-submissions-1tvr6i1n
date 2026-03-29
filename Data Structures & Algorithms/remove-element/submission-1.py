class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
    	i = 0
    	for el in nums:
    		if el!= val:
    			nums[i] = el
    			i+=1
    	return i
        