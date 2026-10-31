class Solution:
    def longestAlternating(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [[0,0] for _ in range(n)] 
        #dp[i][0] ending at i and ending with i-1>i
        #dp1[i][0] starting at i and ending with i<i+1
        dp[0][0] = 1
        dp[0][1] = 1
        for i in range(1, n):
            dp[i][0] = 1
            dp[i][1] = 1
            if nums[i] > nums[i-1]:
                dp[i][1] = dp[i-1][0] + 1
            elif nums[i] < nums[i-1]:
                dp[i][0] = dp[i-1][1] + 1
        dp1 = [[0,0] for _ in range(n)]
        dp1[-1][0] = 1
        dp1[-1][1] = 1
        for i in range(n-2, -1, -1):
            dp1[i][0] = 1
            dp1[i][1] = 1
            if nums[i] < nums[i+1]:
                dp1[i][0] = dp1[i+1][1] + 1
            elif nums[i] > nums[i+1]:
                dp1[i][1] = dp1[i+1][0] + 1
        #a < b > c < d > e < f > h
        print(dp)
        print(dp1)
        res = max(dp[-1][0], dp[-1][1], dp1[0][1], dp1[0][0])
        for i in range(1, n-1):
            if nums[i-1] < nums[i+1]:
                res = max(res, dp[i-1][0] + dp1[i+1][1])
            if nums[i-1] > nums[i+1]:
                res = max(res, dp[i-1][1] + dp1[i+1][0])
        return res
        