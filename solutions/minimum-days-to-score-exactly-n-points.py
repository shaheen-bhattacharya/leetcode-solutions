class Solution:
    def minDays(self, n: int) -> int:
        #dp[i] = min # of days to score i
        upper = 0
        cp = 1
        tmp = n
        while tmp > 0:
            tmp -= cp
            upper += 1
            cp += 1
        
        tri = [0] * (upper+1)
        for i in range(1, upper+1):
            tri[i] = tri[i-1] + i

        dp = [inf] * (n+1)
        dp[0] = 0
            
        for i in range(n+1):
            for l in range(1, upper+1):
                if i + tri[l] > n:
                    break
                dp[i+tri[l]] = min(dp[i+tri[l]], l+1+dp[i])
                
        return dp[n]
                
        
        
        
                
        
        
        