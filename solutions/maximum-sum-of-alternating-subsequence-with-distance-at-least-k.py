class SegTree:
    def __init__(self, n):
        self.n = n
        self.tree = [0] * (4*n)
        
    def update(self, i, val):
        def dfs(node, l, r):
            if l == r:
                self.tree[node] = val
                return 
            m = (l+r)//2
            if i <= m:
                dfs(2*node, l, m)
            else:
                dfs(2*node+1, m+1, r)
            self.tree[node] = max(self.tree[2*node], self.tree[2*node+1])
        dfs(1, 0, self.n-1 )
    
    def query(self, ql, qr):
        def dfs(node, l, r):
            if ql <= l and r <= qr:
                return self.tree[node]
            if r < ql or l > qr:
                return 0
            m = (l+r)//2
            return max(dfs(2*node, l, m), dfs(2*node+1, m+1, r))
        return dfs(1, 0, self.n-1)

class Solution:
    def maxAlternatingSum(self, nums: list[int], k: int) -> int:
        n = len(nums)
        maxv = max(nums)
        #
        dp = [[0,0] for _ in range(n)]
        inc = SegTree(maxv+1)
        dec = SegTree(maxv+1)
        
        for i in range(k):
            dp[i] = [nums[i], nums[i]]
        
        for i in range(k, n):
            inc.update(i-k, dp[i-k][1])
            dec.update(i-k, dp[i-k][0])
            dp[i][0] = inc.query(nums[i]+1, maxv) + nums[i]
            dp[i][1] = dec.query(0, nums[i]-1) + nums[i]
        return max([max(dp[i]) for i in range(n)])


        

            

