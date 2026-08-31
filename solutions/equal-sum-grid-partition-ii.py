class Solution:
    def canPartitionGrid(self, grid: List[List[int]]) -> bool:
        rows, cols = len(grid), len(grid[0])
        def works(arr, flag=True):
            if len(arr) <= 1:
                return False
            acc = 0 
            pref = [0] + list(accumulate(arr))
            ps = set(pref)
            tot = pref[-1]
            print(tot//2, ps)
            if tot//2 in ps:
                return True
            if flag:
                for i in range(len(arr)-1):
                    if pref[i+1] == tot - pref[i+1] - arr[i+1]:
                        return True
            return False

        if rows == 1:
            return works(grid[0]) or works(grid[0][::-1], False) or works(grid[0][1:], False)
        if cols == 1:
            arr = [grid[0][0]]
            for r in range(1, rows):
                arr.append(grid[r][0])
            return works(arr) or works(arr[::-1], False) or works(arr[1:], False)

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
            for c in range(cols):
                top[grid[r][c]] += 1
                bottom[grid[r][c]] -= 1
                rs += grid[r][c]  
            tsum += rs
            bsum -= rs
            if bsum == tsum:
                return True
            diff = abs(bsum-tsum)
            if bsum > tsum:
                if r == rows-2:
                    if (grid[r+1][-1] == diff or grid[r+1][0] == diff):
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
        #vertical
        left = defaultdict(int)
        right = defaultdict(int)
        lsum = 0
        rsum = 0

        for c in range(cols):
            for r in range(rows):
                right[grid[r][c]] += 1
                rsum += grid[r][c]

        for c in range(cols-1):
            rs = 0
            for r in range(rows):
                left[grid[r][c]] += 1
                right[grid[r][c]] -= 1
                rs += grid[r][c] 

            lsum += rs
            rsum -= rs
            # print(lsum, rsum)
            if lsum == rsum:
                return True
            diff = abs(lsum-rsum)
            if rsum > lsum:
                if c == cols-2:
                    # print("d",lsum, rsum)
                    if (grid[0][c+1] == diff or grid[-1][c+1] == diff):
                        return True
                else:
                    if right[diff] > 0:
                        return True
            if rsum < lsum:
                if c == 0:
                    if (grid[0][c] == diff or grid[-1][c] == diff):
                        return True
                else:
                    if left[diff] > 0:
                        return True
        return False
        
        
            


        


        

