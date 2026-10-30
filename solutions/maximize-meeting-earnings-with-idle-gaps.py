class Solution:
    def maxEarnings(self, meetings: list[list[int]]) -> int:
        meetings.sort(key = lambda x:x[0])
        n = len(meetings)
        dp = [0]*n
        dp[0] = meetings[0][2]

        for i in range(1, n):
            l, r, cost = meetings[i]
            dp[i] = cost
            for j in range(i):
                if meetings[j][1] <= l:
                    diff = l - meetings[j][1]
                    dp[i] = max(dp[i], dp[j-1]+cost+diff)
        return max(dp)
                
