class Solution:
    def getOrder(self, tasks):
        n = len(tasks)
        arr = []
        for i in range(n):
            arr.append((tasks[i][0], tasks[i][1], i))
        arr.sort()

        h = []

        def push(x):
            h.append(x)
            i = len(h) - 1
            while i > 0:
                p = (i - 1) // 2
                if h[p] <= h[i]:
                    break
                h[p], h[i] = h[i], h[p]
                i = p

        def pop():
            res = h[0]
            last = h.pop()
            if h:
                h[0] = last
                i = 0
                while True:
                    l = i * 2 + 1
                    r = i * 2 + 2
                    s = i
                    if l < len(h) and h[l] < h[s]:
                        s = l
                    if r < len(h) and h[r] < h[s]:
                        s = r
                    if s == i:
                        break
                    h[i], h[s] = h[s], h[i]
                    i = s
            return res

        ans = []
        time = 0
        i = 0

        while i < n or h:
            if not h and time < arr[i][0]:
                time = arr[i][0]

            while i < n and arr[i][0] <= time:
                push((arr[i][1], arr[i][2]))
                i += 1

            p, idx = pop()
            ans.append(idx)
            time += p

        return ans