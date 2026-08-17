class Solution:
    def elevatorRequests(self, n: int, start: int, requests: list[int]) -> int:
        if len(requests) == 1:
            return abs(start - requests[0])
        requests.sort()
        nr = len(requests)
        l, r = 0, len(requests)
        while l < r:
            m = (l+r)//2
            if requests[m] < start:
                l = m + 1
            else:
                r = m

        dp = [[[-1]*3 for _ in range(nr+2)] for _ in range(nr+2)]
        #i left and j right
        def dfs(i, j, dir):
            if i==-1 and j==nr:
                return 0
            if dp[i][j][dir] != -1:
                return dp[i][j][dir]
    
            rem = i + nr - j + 1
            if dir == 0:
                curr = requests[i + 1]
            elif dir == 1:
                curr = requests[j - 1]
            else:
                curr = start
        
            res = inf
            if i > -1:
                prev = requests[i]
                res = min(res, (curr - prev) * rem + dfs(i-1, j, 0))
                
            if j < nr:
                nxt = requests[j]
                res = min(res, (nxt - curr) * rem + dfs(i, j+1, 1))
            dp[i][j][dir] = res
            return res
        return dfs(l-1, l, 2)                
                
                
                
                
                
            
            
            
        

        
                
        
            
            
        