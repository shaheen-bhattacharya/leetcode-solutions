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
            if i == n:
                return 0 if amt == k else inf
            ret = inf
            t = 0
            ta = 0
            for j in range(i+1, min(i+k-amt, n-1)):
                t += time[j-1]
                ta += 1
                ret = min(ret, t * (position[j] - position[i]) + dfs(j+1, amt + ta))
            dp[key] = ret
            return ret
        return dfs(0,0)


