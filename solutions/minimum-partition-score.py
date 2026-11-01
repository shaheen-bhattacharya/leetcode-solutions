class Solution:
    def minPartitionScore(self, nums: List[int], k: int) -> int:
        n = len(nums)
        def value(num):
            return (num*(num+1))//2

        pref = [0] + list(accumulate(nums))
        dp = {}
        def dfs(i, u):
            key = (i, u)
            if key in dp:
                return dp[key]
            if i == n:
                return 0 if u == k else -inf
            if u > k:
                return -inf

            res = 0
            for j in range(i, n):
                print(i, pref[j+1] - pref[i])
                res = max(res, dfs(j+1, u+1) + value(pref[j+1] - pref[i]))
            dp[key] = res
            return res
        return dfs(0, 0)

