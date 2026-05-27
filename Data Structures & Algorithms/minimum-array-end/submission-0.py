class Solution:
    def minEnd(self, n: int, x: int) -> int:
        res = x
        bit_x = 1
        bit_n = 1
        target = n - 1

        while bit_n <= target:
            if (x & bit_x) == 0:
                if target & bit_n:
                    res |= bit_x
                bit_n <<= 1
            bit_x <<= 1

        return res