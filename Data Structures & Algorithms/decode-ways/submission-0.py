class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        if s[0] == "0":
            return 0

        dp1, dp2 = 1, 1

        for i in range(1, n):
            curr = 0

            if s[i] != "0":
                curr += dp2

            if 10 <= int(s[i - 1:i + 1]) <= 26:
                curr += dp1

            dp1, dp2 = dp2, curr

        return dp2