class Solution:
    def minCost(self, nums: list[int]) -> int:
        dp = {}
        """
       -9, 3, -50, 1, 8, -3, -5, -50, 6, 8, -50, 9, -4, 8, -7, 5, 9, 3
        """
        n=len(nums) 
        dp = [[inf]*2 for _ in range(n)]
        dp[0][0] = inf
        dp[0][1] = nums[0]
        
        for i in range(1, n):
            dp[i][0] = min(dp[i][0], dp[i-1][0], dp[i-1][1] + nums[i])
            dp[i][1] = min(dp[i][1], dp[i-1][1], dp[i-1][0] + nums[i])
        return dp[-1][0]
        
            