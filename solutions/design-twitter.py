from collections import defaultdict
import heapq

class Twitter:

    def __init__(self):
        self.time = 0
        self.tweets = defaultdict(list)
        self.following = defaultdict(set)

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets[userId].append((self.time, tweetId))
        self.time += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        heap = []
        users = self.following[userId] | {userId}

        for user in users:
            if self.tweets[user]:
                i = len(self.tweets[user]) - 1
                t, tid = self.tweets[user][i]
                heapq.heappush(heap, (-t, tid, user, i-1))

        res = []
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
        self.following[followerId].discard(followeeId)