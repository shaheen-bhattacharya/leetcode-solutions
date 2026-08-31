class Twitter:

    def __init__(self):
        self.time = 0
        self.following = defaultdict(set)
        self.tweets = defaultdict(list)

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets[userId].append((self.time, tweetId))
        self.time += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        heap = []
        users = self.following[userId] | {userId}
        res = []
        for user in users:
            i = len(self.tweets[user]) - 1
            t, tid = self.tweets[user][i]
            heapq.heappush(heap, (-t, tid, user, i-1))
        
        while heap and len(res) < 10:
            nt, tid, user, i = heapq.heappop(heap)
            res.append(tid)
            if i >= 0:
                t, tid = self.tweets[user][i]
                heapq.heappush(heap, (-t, tid, user, i-1))
        return res


    def follow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].remove(followeeId)


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)