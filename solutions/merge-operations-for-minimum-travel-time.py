class Solution:
    def minTravelTime(self, l: int, n: int, k: int, position: List[int], time: List[int]) -> int:
        """
        3 5 2
        5 8 3
        """
        dp = {}
        pref = [0] + list(accumulate(time))
        def dfs(i, amt, pi):
            key = (i, amt, pi)
            if key in dp:
                return dp[key]
            if i == n-1:
                return 0 if amt == k else inf
            if amt > k:
                return inf
            
            rate = pref[i+1] - pref[pi+1]
            ret = inf
            t = 0
            for j in range(i+1, n):
                dist = position[j] - position[i]
                ret = min(ret, dist * rate + dfs(j, amt+j-i-1, i))
            dp[key] = ret
            return ret
        return dfs(0,0,-1)


