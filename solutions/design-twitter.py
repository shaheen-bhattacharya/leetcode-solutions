class Twitter:

    def __init__(self):
        self.posts = defaultdict(deque)
        self.followers = defaultdict(set)
        self.following = defaultdict(set)

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.posts[userId].appendleft(tweetId)
        if len(self.posts[userId]) > 10:
            self.posts[userId].pop()

        for nei in self.followers[userId]:
            self.posts[nei].appendleft(tweetId)
            if len(self.posts[nei]) > 10:
                self.posts[nei].pop()

    def getNewsFeed(self, userId: int) -> List[int]:
        return list(self.posts[userId])
        
    def follow(self, followerId: int, followeeId: int) -> None:
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