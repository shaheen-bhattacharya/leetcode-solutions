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

            left, right = l, r 
            tot = pref[r+1] - pref[l]
            while left < right:
                mid = (left + right) // 2
                if 2 * (pref[mid + 1] - pref[l]) < tot:
                    left = mid + 1
                else: 
                    right = mid

            rsum = pref[r+1] - pref[mid]
            lsum = pref[mid+1] - pref[l]
            dp[l][r] = max(lsum + dfs(l, mid), rsum + dfs(mid+1, r))

            return dp[l][r]
            
        return dfs(0, n-1)