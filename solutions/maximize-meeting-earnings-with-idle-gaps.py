class Solution:
    def maxEarnings(self, meetings: list[list[int]]) -> int:
        meetings.sort(key = lambda x:x[0])
        n = len(meetings)
        dp = [0]*n
        dp[0] = meetings[0][2]
        sl = SortedList([(meetings[0][1], 0)])

        for i in range(1, n):
            l, r, cost = meetings[i]
            dp[i] = cost
            idx = sl.bisect_right((l, n))
            print(sl, idx)

            for j in range(idx):
                r, k = sl[j]
                diff = l - r
                dp[i] = max(dp[i], dp[k]+cost+diff)
            sl.add((r, i))
        return max(dp)
                
