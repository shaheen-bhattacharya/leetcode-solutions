class Solution:
    def stoneGameV(self, stoneValue: List[int]) -> int:
        dp = {}
        n = len(stoneValue)
        pref = [0] + list(accumulate(stoneValue))
        def dfs(l, r):
            key = (l, r)
            if key in dp:
                return dp[key]
            if r - l == 1:
                return 0
            res = 0
            lsum = 0
            rsum = pref[r+1] - pref[l]
            for i in range(l, r+1):
                lsum += stoneValue[i]
                rsum -= stoneValue[i]
                if lsum > rsum:
                    res = max(res, rsum + dfs(i+1, r))
                else:
                    res = max(res, lsum + dfs(0, i))
            dp[key] = res
            return res
            
        return dfs(0, n-1)