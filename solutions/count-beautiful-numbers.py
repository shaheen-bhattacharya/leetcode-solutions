class Solution:
    def beautifulNumbers(self, l: int, r: int) -> int:
        """
        123 == 321
        """
        def solve(num):
            snum = str(num)
            n = len(snum)
            dp = {}
            def dfs(i, zero, tight, prod, tot):
                key = (i, zero, tight, prod, tot)
                if key in dp:
                    return dp[key]
                if i == n:
                    if zero:
                        return 0
                    else:
                        if prod % tot == 0 and num == 20:
                            print(prod, tot)
                        return prod % tot == 0
                digit = int(snum[i])
                upper = digit if tight else 9
                ret = 0
                for j in range(upper+1):
                    nt = False
                    if tight and j == digit:
                        nt = True
                    ret += dfs(i+1,zero and j==0, nt, prod * j, tot + j)
                dp[key] = ret
                return ret
            return dfs(0, True, True, 1, 0)
        return solve(r) - solve(l-1)
                

                


