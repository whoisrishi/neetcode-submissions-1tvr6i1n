class FreqStack:

    def __init__(self):
        self.cnt = {}
        self.group = {}
        self.maxFreq = 0

    def push(self, val: int) -> None:
        if val in self.cnt:
            self.cnt[val] += 1
        else:
            self.cnt[val] = 1
        
        freq = self.cnt[val]

        if freq > self.maxFreq:
            self.maxFreq = freq

        if freq not in self.group:
            self.group[freq] = []
        self.group[freq].append(val)

    def pop(self) -> int:
        val = self.group[self.maxFreq].pop()
        self.cnt[val] -= 1

        if len(self.group[self.maxFreq]) == 0:
            self.maxFreq -= 1

        return val