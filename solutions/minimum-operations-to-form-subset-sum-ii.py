from math import inf

class Solution:
    def minOperations(self, nums: list[int], sm: int) -> int:
        inf_val = 10**9
        dp = [inf_val] * (sm + 1)
        dp[0] = 0
        
        for x in nums:
            ndp = dp[:]
            for w in range(sm, -1, -1):
                if dp[w] == inf_val:
                    continue
                
                # Option 1: Only multiply (or keep x)
                i, y = 0, x
                while y <= sm:
                    if w + y <= sm:
                        ndp[w + y] = min(ndp[w + y], dp[w] + i)
                    i += 1
                    y *= 2
                
                # Option 2: Divide at least once, then optionally multiply
                i, y = 1, x // 2
                while y > 0:
                    j, z = 0, y
                    while z <= sm:
                        if w + z <= sm:
                            ndp[w + z] = min(ndp[w + z], dp[w] + i + j)
                        j += 1
                        z *= 2
                    i += 1
                    y //= 2
                    
            dp = ndp

        return dp[sm] if dp[sm] != inf_val else -1