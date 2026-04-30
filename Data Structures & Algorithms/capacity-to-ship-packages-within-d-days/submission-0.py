class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        
        def canShip(cap):
            d = 1
            curr = 0
            
            for w in weights:
                if curr + w > cap:
                    d += 1
                    curr = 0
                curr += w
            
            return d <= days
        
        left, right = max(weights), sum(weights)
        res = right
        
        while left <= right:
            mid = (left + right) // 2
            
            if canShip(mid):
                res = mid
                right = mid - 1   
            else:
                left = mid + 1    
        
        return res