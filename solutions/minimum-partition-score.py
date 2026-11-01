class Solution:
    def minPartitionScore(self, nums: List[int], k: int) -> int:
        n = len(nums)
        def value(num):
            return (num*(num+1))//2
        
        dp = [[inf] * (k+1) for _ in range(n+1)]
        pref = [0] + list(accumulate(nums))

        dp[n][k] = 0
        for i in range(n-1, -1, -1):
            for j in range(i, n):
                for u in range(k):
                    dp[i][u] = min(dp[i][u], dp[j+1][u+1] + value(pref[j+1] - pref[i]))
        return dp[0][0]

        # dp = {}
        # def dfs(i, u):
        #     key = (i, u)
        #     if key in dp:
        #         return dp[key]
        #     if i == n:
        #         return 0 if u == k else inf
        #     if u > k:
        #         return inf
        #     res = inf
        #     for j in range(i, n):
        #         res = min(res, dfs(j+1, u+1) + value(pref[j+1] - pref[i]))
        #     dp[key] = res
        #     return res
        # return dfs(0, 0)

