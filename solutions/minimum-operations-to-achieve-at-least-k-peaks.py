class Solution:
    def minOperations(self, nums: list[int], k: int) -> int:
        """
        6 4 5 3 6 4
        """
        if k == 0:
            return 0
        nums = [nums[-1]] + nums + [nums[0]]
        n = len(nums)
        if k > (n-2)//2:
            return -1
        amt = 0
        for i in range(1, n-1):
            if nums[i] > nums[i-1] and nums[i] > nums[i+1]:
                amt += 1
        if amt >= k:
            return 0
        #dp[i][j] = at index i min cost to j peaks
        dp = [[inf]*(k+1) for _ in range(n-1)]
        
        def mc(i):
            if i == 1:
                l, m, r = nums[n-2], nums[i], nums[i+1]
            elif i == n-2:
                l, m, r = nums[i-1], nums[i], nums[1]
            else:
                l, m, r = nums[i-1], nums[i], nums[i+1]
            return max(0, max(l, r)+1-m)
        # print(mc(3))
        #select i=1
        dp[0][0] = 0
        dp[2][1] = mc(1)
        dp[1][1] = mc(1)
        for i in range(3, n-1):
            for j in range(k+1):
                dp[i][j] = dp[i-1][j]
                if j > 0:
                    dp[i][j] = min(dp[i][j], dp[i-2][j-1] + mc(i))

        res = dp[n-2][k]

        dp = [[inf]*(k+1) for _ in range(n-1)]
        dp[0][0] = 0
        dp[1][0] = 0
        dp[1][1] = inf

        for i in range(2, n-1):
            for j in range(k+1):
                dp[i][j] = dp[i-1][j]
                if j > 0:
                    dp[i][j] = min(dp[i][j], dp[i-2][j-1] + mc(i))
        res = min(res, dp[n-2][k])
        return res 
        


