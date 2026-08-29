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

        # Include the user's own tweets
        users = self.following[userId] | {userId}

        # Add newest tweet from each user
        for user in users:
            if self.tweets[user]:
                i = len(self.tweets[user]) - 1
                time, tweetId = self.tweets[user][i]

                # Negative because heapq is a min-heap
                heapq.heappush(
                    heap,
                    (time, tweetId, user, i - 1)
                )

        res = []

        # K-way merge, stopping after 10 tweets
        while heap and len(res) < 10:
            t, tweetId, user, i = heapq.heappop(heap)
            res.append(tweetId)

            # Add next-oldest tweet from this user
            if i >= 0:
                time, tweetId = self.tweets[user][i]

                heapq.heappush(
                    heap,
                    (time, tweetId, user, i - 1)
                )

        return res[::]

    def follow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].discard(followeeId)