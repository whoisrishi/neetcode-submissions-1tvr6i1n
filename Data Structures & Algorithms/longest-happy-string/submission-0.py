class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        cnt = [[a, "a"], [b, "b"], [c, "c"]]
        res = []

        while True:
            cnt.sort(reverse=True)
            used = False

            for i in range(3):
                if cnt[i][0] == 0:
                    continue
                ch = cnt[i][1]
                if len(res) >= 2 and res[-1] == ch and res[-2] == ch:
                    continue
                res.append(ch)
                cnt[i][0] -= 1
                used = True
                break

            if not used:
                break

        return "".join(res)