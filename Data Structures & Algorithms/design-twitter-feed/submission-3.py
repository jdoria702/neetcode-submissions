class Twitter:

    def __init__(self):
        self.posts = {}
        self.following = {}
        self.time = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        user_posts = self.posts.get(userId, [])
        user_posts.append((self.time, tweetId))
        self.posts[userId] = user_posts
        self.time = self.time - 1
        return
        

    def getNewsFeed(self, userId: int) -> List[int]:
        # Maintain heap of most recent posts (max heap)
        heap = []

        # Initialize heap with the most recent post from the userId and post from following
        # Node in heap (time, tweetId, userId, index)
        if self.posts.get(userId):
            user_posts = self.posts[userId]
            time, tweetId = user_posts[-1]
            idx = len(user_posts) - 1
            heapq.heappush(heap, (time, tweetId, userId, idx))

        user_following = self.following.get(userId, None)
        if user_following:
            for following in user_following:
                if self.posts.get(following):
                    user_posts = self.posts[following]
                    time, tweetId = user_posts[-1]
                    idx = len(user_posts) - 1
                    heapq.heappush(heap, (time, tweetId, following, idx))

        # Pop from heap and add tweetId to result
        # Get the next most recent post from the popped userId
        res = []
        while heap and len(res) < 10:
            popped = heapq.heappop(heap)
            popped_tweetId = popped[1]
            popped_user = popped[2]
            next_idx = popped[3] - 1

            res.append(popped_tweetId)

            if next_idx >= 0:
                user_posts = self.posts[popped_user]
                time, tweetId = user_posts[next_idx]
                heapq.heappush(heap, (time, tweetId, popped_user, next_idx))

        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        user_following = self.following.get(followerId, set())
        if followerId != followeeId:
            user_following.add(followeeId)
        self.following[followerId] = user_following
        return
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        user_following = self.following.get(followerId)
        if followeeId in user_following:
            user_following.remove(followeeId)
        self.following[followerId] = user_following
        return
        
