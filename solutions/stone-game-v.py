class Solution:
    def stoneGameV(self, stoneValue: List[int]) -> int:
        dp = {}
        n = len(stoneValue)
        pref = [0] + list(accumulate(stoneValue))
        dp = [[-1] * n for _ in range(n)]
        def dfs(l, r):
            if r - l <= 0:
                return 0
            if dp[l][r] != -1:
                return dp[l][r]
            res = 0
            lsum = 0
            rsum = pref[r+1] - pref[l]
            for i in range(l, r+1):
                lsum += stoneValue[i]
                rsum -= stoneValue[i]
                if lsum > rsum:
                    res = max(res, rsum + dfs(i+1, r))
                elif rsum > lsum:
                    res = max(res, lsum + dfs(l, i))
                else:
                    res = max(res, lsum + dfs(l, i), rsum + dfs(i+1, r))
            dp[l][r] = res
            return res
            
        return dfs(0, n-1)