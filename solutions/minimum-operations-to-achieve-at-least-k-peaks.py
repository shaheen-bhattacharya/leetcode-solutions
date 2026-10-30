class Solution:
    def minOperations(self, nums: list[int], k: int) -> int:
        """
        6 4 5 3 6 4
        """
        nums = [nums[-1]] + nums + [nums[0]]
        n = len(nums)
        amt = 0
        for i in range(1, n-1):
            if nums[i] > nums[i-1] and nums[i] > nums[i+1]:
                amt += 1
        if amt >= k:
            return 0
        #dp[i][j] = at index i min cost to j peaks
        dp = [[inf]*(k+1) for _ in range(n-1)]
        dp[0][0] = 0
        
        def mc(i):
            if i == 1:
                l, m, r = nums[n-2], nums[i], nums[i+1]
            elif i == n-2:
                l, m, r = nums[i-1], nums[i], nums[1]
            else:
                l, m, r = nums[i-1], nums[i], nums[i+1]
            return max(0, max(l, r)+1-m)
        
        for i in range(1, n-1):
            for j in range(k+1):
                dp[i][j] = min(dp[i][j-1], dp[i-2][j-1] + mc(i))
        
        # dp[1][0] = 0
        # dp[1][1] = mc(i)

        res = inf
        for i in range(1, n-1):
            res = min(res, dp[i][k])
        return res if res != inf else -1
        


