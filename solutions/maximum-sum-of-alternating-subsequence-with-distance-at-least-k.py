class Solution:
    def maxAlternatingSum(self, nums: list[int], k: int) -> int:
        n = len(nums)
        maxv = max(nums)
        #dp[i][val][1] max sum from [:i+1] with next being increasing or decreasing
        dp = [[[0,0] for _ in range(maxv+1)] for _ in range(n)] 
        mv = 0      
        dp[0][nums[0]] = [nums[0], nums[0]]     
        for i in range(1, k):
            for v in range(maxv+1):
                dp[i][v] = dp[i-1][v][:]

        for i in range(k, n):
            for v in range(maxv+1):
                dp[i][v] = dp[i-1][v][:]
            for v in range(nums[i]):
                dp[i][nums[i]][0] = max(dp[i][nums[i]][0], dp[i-k][v][1] + nums[i])
            for v in range(nums[i]+1, maxv+1):
                dp[i][nums[i]][1] = max(dp[i][nums[i]][1], dp[i-k][v][0] + nums[i])
        res = 0
        for i in range(n):
            for v in range(maxv+1):
                res = max(res, max(dp[i][v]))
        return res
            

