class Twitter:

    def __init__(self):
        self.time = 0
        self.tweets = {}
        self.following = {}

    def postTweet(self, userId: int, tweetId: int) -> None:
        if userId not in self.tweets:
            self.tweets[userId] = []
        self.tweets[userId].append((self.time, tweetId))
        self.time -= 1

    def getNewsFeed(self, userId: int) -> List[int]:
        if userId not in self.following:
            self.following[userId] = set()
        self.following[userId].add(userId)

        heap = []

        def push(x):
            heap.append(x)
            i = len(heap) - 1
            while i:
                p = (i - 1) // 2
                if heap[p][0] <= heap[i][0]:
                    break
                heap[p], heap[i] = heap[i], heap[p]
                i = p

        def pop():
            res = heap[0]
            last = heap.pop()
            if heap:
                heap[0] = last
                i = 0
                n = len(heap)
                while True:
                    l = i * 2 + 1
                    r = l + 1
                    s = i
                    if l < n and heap[l][0] < heap[s][0]:
                        s = l
                    if r < n and heap[r][0] < heap[s][0]:
                        s = r
                    if s == i:
                        break
                    heap[i], heap[s] = heap[s], heap[i]
                    i = s
            return res

        for uid in self.following[userId]:
            if uid in self.tweets and self.tweets[uid]:
                idx = len(self.tweets[uid]) - 1
                t, tid = self.tweets[uid][idx]
                push((t, tid, uid, idx - 1))

        res = []
        while heap and len(res) < 10:
            t, tid, uid, idx = pop()
            res.append(tid)
            if idx >= 0:
                nt, ntid = self.tweets[uid][idx]
                push((nt, ntid, uid, idx - 1))

        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId not in self.following:
            self.following[followerId] = set()
        self.following[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId in self.following and followeeId != followerId:
            self.following[followerId].discard(followeeId)