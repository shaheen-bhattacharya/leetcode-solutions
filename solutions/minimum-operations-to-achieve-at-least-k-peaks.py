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
            l, m, r = nums[i-1], nums[i], nums[i+1]
            return max(0, max(l, r)+1-m)
        
        for i in range(1, n-1):
            for j in range(k+1):
                cst = dp[i-2][j-1] if i >= 2 else dp[i-1][j-1]
                dp[i][j] = min(dp[i][j], cst + mc(i))

        res = inf
        for i in range(1, n-1):
            res = min(res, dp[i][k])
        return res if res != inf else -1
        


