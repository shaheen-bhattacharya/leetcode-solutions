class Solution:
    def canPartitionGrid(self, grid: List[List[int]]) -> bool:
        rows, cols = len(grid), len(grid[0])
        dp = [0]*(cols+1)

        for r in range(rows):
            ndp = [0]*(cols+1)
            pref = [0] + list(accumulate(grid[r]))
            tot = pref[-1]
            for c in range(cols+1):
                ndp[c] = dp[c] + tot - 2 * pref[c]
                if r == rows-1 and ndp[c] == 0:
                    return True
            dp = ndp
            # print(dp)
        return False
