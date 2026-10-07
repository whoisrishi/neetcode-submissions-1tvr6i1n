class Solution:
    def openLock(self, deadends, target):
        dead = set(deadends)
        if "0000" in dead:
            return -1

        q = ["0000"]
        seen = {"0000"}
        moves = 0

        while q:
            for _ in range(len(q)):
                cur = q.pop(0)

                if cur == target:
                    return moves

                for i in range(4):
                    d = int(cur[i])

                    for nd in ((d + 1) % 10, (d - 1) % 10):
                        nxt = cur[:i] + str(nd) + cur[i + 1:]

                        if nxt not in dead and nxt not in seen:
                            seen.add(nxt)
                            q.append(nxt)

            moves += 1

        return -1