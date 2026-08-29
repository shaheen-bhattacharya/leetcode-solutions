class Twitter:

    def __init__(self):
        self.posts = defaultdict(deque)
        self.corr = {}
        self.followers = defaultdict(set)
        self.following = defaultdict(set)
        self.time = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.posts[userId].appendleft((self.time, tweetId))
        self.corr[tweetId] = userId
        self.time += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        ret = []
        heap = []
        users = list(self.following[userId]) + [userId]

        for uf in users:
            tmp = self.posts[uf].copy()
            while tmp:
                t, tid = tmp.popleft()
                heapq.heappush(heap, (-t, tid))
                if len(heap) > 10:
                    heapq.heappop(heap)
        while heap:
            t, tid = heapq.heappop(heap)
            ret.append(tid)
        return ret

    def follow(self, followerId: int, followeeId: int) -> None:
        if followeeId not in self.following[followerId]:
            self.following[followerId].add(followeeId)
            self.followers[followeeId].add(followerId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].discard(followeeId)
        self.followers[followeeId].discard(followerId)


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)