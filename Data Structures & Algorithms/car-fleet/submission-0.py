class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pair = sorted(zip(position, speed), reverse=True)
        fleets = 0
        prev_time = 0
        
        for p, s in pair:
            time = (target - p) / s
            if time > prev_time:
                fleets += 1
                prev_time = time
        
        return fleets