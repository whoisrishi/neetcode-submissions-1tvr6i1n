class Solution:
    def minMeetingRooms(self, intervals):
        intervals.sort(key=lambda x: x.start)
        heap = []

        def push(x):
            heap.append(x)
            i = len(heap) - 1
            while i > 0:
                p = (i - 1) // 2
                if heap[p] <= heap[i]:
                    break
                heap[p], heap[i] = heap[i], heap[p]
                i = p

        def pop():
            heap[0] = heap[-1]
            heap.pop()
            i = 0
            n = len(heap)
            while True:
                l = 2 * i + 1
                r = 2 * i + 2
                s = i
                if l < n and heap[l] < heap[s]:
                    s = l
                if r < n and heap[r] < heap[s]:
                    s = r
                if s == i:
                    break
                heap[i], heap[s] = heap[s], heap[i]
                i = s

        for interval in intervals:
            if heap and heap[0] <= interval.start:
                pop()
            push(interval.end)

        return len(heap)