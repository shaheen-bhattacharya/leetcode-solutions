class Solution:
    def maximumSum(self, nums: List[int], m: int, l: int, r: int) -> int:
        n = len(nums)
        pref = [0] + list(accumulate(nums))
        dp = [[-inf]*(m+1) for _ in range(n+1)]
        dp[0][0] = 0

        for i in range(1, n+1):
            for j in range(m+1):
                dp[i][j] = dp[i-1][j]
                for k in range(i-l, max(-1, i-r-1), -1):
                    if k < 0:
                        continue
                    if j > 0:
                        dp[i][j] = max(dp[i][j], dp[k][j-1]+pref[i]-pref[k])
        res = -inf
        for i in range(m+1):
            res = max(res, dp[-1][i])
        return res
