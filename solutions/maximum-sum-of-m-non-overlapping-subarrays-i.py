class Solution:
    def maximumSum(self, nums: List[int], m: int, l: int, r: int) -> int:
        n = len(nums)
        pref = [0] + list(accumulate(nums))
        dp = [[-inf]*(m+1) for _ in range(n+1)]
        dp[0][0] = 0
        # q = deque([(0,0)])

        for i in range(1, n+1):
            q = deque()
            for j in range(m+1):
                dp[i][j] = dp[i-1][j]
                if j == 0:
                    continue
                    
                if i-l >= 0:
                    nv = dp[i-l][j-1] - pref[i-l]
                    while q and nv > q[-1][1]:
                        q.pop()
                    q.append((i-l, nv))
                    if q[0][0] <= i-r-1:
                        q.popleft()
                    dp[i][j] = max(dp[i][j], pref[i] + q[0][1])
                
        res = -inf
        for i in range(1, m+1):
            res = max(res, dp[-1][i])
        return res
