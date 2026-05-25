class Solution:
    def getSum(self, a: int, b: int) -> int:
        MASK = 0xffffffff
        MAX = 0x7fffffff

        while b != 0:
            a, b = (a ^ b) & MASK, ((a & b) << 1) & MASK

        return a if a <= MAX else ~(a ^ MASK)