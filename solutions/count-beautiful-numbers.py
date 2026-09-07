class Solution:
    def beautifulNumbers(self, l: int, r: int) -> int:
        """
        123 == 321
        """
        def solve(num):
            snum = str(num)
            n = len(snum)
            dp = {}
            def dfs(i, tight, prod, tot):
                key = (i, tight, prod, tot)
                if key in dp:
                    return dp[key]
                if i == n:
                    return tot == 0 or prod % tot == 0
                digit = int(snum[i])
                upper = digit if tight else 9
                lower = 1 if i == 0 else 0
                ret = 0
                for j in range(lower, upper+1):
                    nt = False
                    if tight and j == digit:
                        nt = True
                    ret += dfs(i+1, nt, prod * j, tot + j)
                dp[key] = ret
                return ret
            return dfs(0, True, 1, 0)
        return solve(r) - solve(l-1)
                

                


