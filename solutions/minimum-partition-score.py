class Solution:
    def minPartitionScore(self, nums: List[int], k: int) -> int:
        n = len(nums)
        #dp[i][j] = min score ending at i with j subarrays
        def value(num):
            return (num*(num+1))//2

        dp = [[inf]*(k+1) for _ in range(n)]
        dp[0][1] = value(nums[0])
        pref = [0] + list(accumulate(nums))
        for i in range(1, n):
            for j in range(i):
                for u in range(1, k+1):
                    dp[i][u] = min(dp[i][u], dp[j][u] + value(pref[i] - pref[j]), dp[j][u-1] + value(pref[i] - pref[j]))
        print(dp)
        return dp[-1][k]

