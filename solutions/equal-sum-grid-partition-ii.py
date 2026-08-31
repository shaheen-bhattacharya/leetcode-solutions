class Solution:
    def canPartitionGrid(self, grid: List[List[int]]) -> bool:
        rows, cols = len(grid), len(grid[0])

        top = defaultdict(int)
        bottom = defaultdict(int)
        tsum = 0
        bsum = 0

        for row in grid:
            for c in range(cols):
                bottom[row[c]] += 1
                bsum += row[c]
        

        for r in range(rows-1):
            rs = 0
            cb = set()
            ct = set()
            for c in range(cols):
                top[grid[r][c]] += 1
                bottom[grid[r][c]] -= 1
                rs += grid[r][c]  
            tsum += rs
            bsum -= rs
            if bsum == tsum:
                return True
            diff = max(bsum, tsum) - min(bsum, tsum)
            if bsum > tsum:
                if r == rows-2:
                    if (grid[r][-1] == diff or grid[r][0] == diff):
                        return True
                else:
                    if bottom[diff] > 0:
                        return True
            if bsum < tsum:
                if r == 0:
                    if (grid[r][0] == diff or grid[r][-1] == diff):
                        return True
                else:
                    if top[diff] > 0:
                        return True
        return False
            


        


        

