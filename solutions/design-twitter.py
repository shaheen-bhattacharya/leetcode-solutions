class Twitter:

    def __init__(self):
        self.posts = defaultdict(deque)
        self.feed = defaultdict(deque)
        self.corr = {}
        self.followers = defaultdict(set)
        self.following = defaultdict(set)

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.posts[userId].appendleft(tweetId)
        self.feed[userId].appendleft(tweetId)
        self.corr[tweetId] = userId

        for nei in self.followers[userId]:
            self.feed[nei].appendleft(tweetId)

    def getNewsFeed(self, userId: int) -> List[int]:
        ret = []
        count = 0
        for t in self.feed[userId]:
            if count == 10:
                break
            user = self.corr[t]
            if user not in self.following[userId] and user != userId:
                continue
            ret.append(t)
            count += 1
        return ret
        
    def follow(self, followerId: int, followeeId: int) -> None:
        if followeeId not in self.following:
            self.following[followerId].add(followeeId)
            self.followers[followeeId].add(followerId)
            tmp = self.posts[followeeId].copy()
            while tmp:
                self.feed[followerId].appendleft(tmp.pop())

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].discard(followeeId)
        self.followers[followeeId].discard(followerId)


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)