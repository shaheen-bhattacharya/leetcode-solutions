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
                time, tweetId = self.tweets[user][i]

                heapq.heappush(heap, (time, tweetId, user, i - 1))

        res = []

        while heap and len(res) < 10:
            time, tweetId, user, i = heapq.heappop(heap)
            res.append(tweetId)

            if i >= 0:
                time, tweetId = self.tweets[user][i]

                heapq.heappush(
                    heap,
                    (time, tweetId, user, i - 1)
                )

        return res[::-1]

    def follow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].discard(followeeId)