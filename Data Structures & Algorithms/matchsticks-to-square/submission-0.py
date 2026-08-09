class Solution:
    def makesquare(self, matchsticks):
        total = sum(matchsticks)

        if total % 4:
            return False

        side = total // 4
        matchsticks.sort(reverse=True)
        sides = [0] * 4

        def backtrack(i):
            if i == len(matchsticks):
                return True

            stick = matchsticks[i]

            for j in range(4):
                if sides[j] + stick > side:
                    continue

                if j > 0 and sides[j] == sides[j - 1]:
                    continue

                sides[j] += stick

                if backtrack(i + 1):
                    return True

                sides[j] -= stick

            return False

        return backtrack(0)