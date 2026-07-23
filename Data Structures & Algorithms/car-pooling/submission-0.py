class Solution:
    def carPooling(self, trips, capacity):
        diff = [0] * 1002
        for p, s, e in trips:
            diff[s] += p
            diff[e] -= p
        cur = 0
        for x in diff:
            cur += x
            if cur > capacity:
                return False
        return True