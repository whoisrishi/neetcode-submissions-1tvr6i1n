class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        meetings.sort()
        available = list(range(n))
        busy = []
        heapq.heapify(available)
        cnt = [0] * n

        for s, e in meetings:
            while busy and busy[0][0] <= s:
                _, room = heapq.heappop(busy)
                heapq.heappush(available, room)

            if available:
                room = heapq.heappop(available)
                heapq.heappush(busy, (e, room))
            else:
                end, room = heapq.heappop(busy)
                heapq.heappush(busy, (end + e - s, room))

            cnt[room] += 1

        ans = 0
        for i in range(1, n):
            if cnt[i] > cnt[ans]:
                ans = i
        return ans