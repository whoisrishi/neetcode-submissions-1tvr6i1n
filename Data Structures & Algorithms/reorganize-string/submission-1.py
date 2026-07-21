class Solution:
    def reorganizeString(self, s: str) -> str:
        cnt = [0] * 26
        for c in s:
            cnt[ord(c) - 97] += 1

        if max(cnt) > (len(s) + 1) // 2:
            return ""

        ans = []

        while True:
            a = -1
            b = -1

            for i in range(26):
                if cnt[i] > 0:
                    if a == -1 or cnt[i] > cnt[a]:
                        b = a
                        a = i
                    elif b == -1 or cnt[i] > cnt[b]:
                        b = i

            if a == -1:
                break

            ans.append(chr(a + 97))
            cnt[a] -= 1

            if b == -1:
                if cnt[a]:
                    return ""
                break

            ans.append(chr(b + 97))
            cnt[b] -= 1

        return "".join(ans)