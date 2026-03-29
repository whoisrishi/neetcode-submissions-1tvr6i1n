class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        cn1,cn2,c1,c2 = 0,0,None,None
        for n in nums:
            if n == c1:
                cn1+=1
            elif n == c2:
                cn2+=1
            elif cn1 == 0:
                c1,cn1 = n,1
            elif cn2 == 0:
                c2,cn2 = n,1
            else:
                cn1-=1
                cn2-=1
        res = []
        for c in set([c1,c2]):
            if c is not None and nums.count(c)> len(nums) // 3:
                res.append(c)
        return res