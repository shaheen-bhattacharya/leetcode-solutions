class Solution:
    def minTravelTime(self, l: int, n: int, k: int, position: List[int], time: List[int]) -> int:
        """
        3 5 2
        5 8 3
        """
        dp = {}
        def dfs(i, amt):
            key = (i, amt)
            if key in dp:
                return dp[key]
            if i == n-1:
                return 0 if amt == k else inf
            if amt > k:
                return inf
            ret = inf
            t = 0
            for j in range(i+1, n):
                t += time[j-1]
                ret = min(ret, t * (position[j] - position[i+1]) + dfs(j, amt+j-i-1))
            dp[key] = ret
            return ret
        return dfs(0,0)


