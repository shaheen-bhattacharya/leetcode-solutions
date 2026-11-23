class Solution:
    def minCost(self, nums: list[int]) -> int:
        dp = {}
        """
       -9, 3, -50, 1, 8, -3, -5, -50, 6, 8, -50, 9, -4, 8, -7, 5, 9, 3
        """
        n=len(nums) 
        res = nums[0] + nums[-1]
        if n == 2:
            return res

        dp = [[inf]*2 for _ in range(n)]
        dp[1][0] = 0
        dp[1][1] = nums[1]
        for i in range(2, n-1):
            dp[i][0] = min(dp[i-1][0], dp[i-1][1] + nums[i])
            dp[i][1] = min(dp[i-1][1], dp[i-1][0] + nums[i])
        return dp[-2][0] + res
        
            