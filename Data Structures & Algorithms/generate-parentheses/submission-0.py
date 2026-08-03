class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        res = []

        def dfs(cur, open_cnt, close_cnt):
            if len(cur) == 2 * n:
                res.append(cur)
                return
            if open_cnt < n:
                dfs(cur + "(", open_cnt + 1, close_cnt)
            if close_cnt < open_cnt:
                dfs(cur + ")", open_cnt, close_cnt + 1)

        dfs("", 0, 0)
        return res