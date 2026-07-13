class KthLargest:

    def __init__(self, k: int, nums: list[int]):
        self.k = k
        self.h = nums[:]
        n = len(self.h)
        for i in range(n // 2 - 1, -1, -1):
            self.down(i)
        while len(self.h) > k:
            self.pop()

    def add(self, val: int) -> int:
        self.h.append(val)
        self.up(len(self.h) - 1)
        if len(self.h) > self.k:
            self.pop()
        return self.h[0]

    def up(self, i):
        while i:
            p = (i - 1) // 2
            if self.h[p] <= self.h[i]:
                break
            self.h[p], self.h[i] = self.h[i], self.h[p]
            i = p

    def down(self, i):
        n = len(self.h)
        while True:
            l = 2 * i + 1
            r = l + 1
            s = i
            if l < n and self.h[l] < self.h[s]:
                s = l
            if r < n and self.h[r] < self.h[s]:
                s = r
            if s == i:
                break
            self.h[i], self.h[s] = self.h[s], self.h[i]
            i = s

    def pop(self):
        self.h[0], self.h[-1] = self.h[-1], self.h[0]
        self.h.pop()
        if self.h:
            self.down(0)