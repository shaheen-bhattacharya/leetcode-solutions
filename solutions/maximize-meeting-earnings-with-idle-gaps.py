class SegTree:
    def __init__(self, n):
        self.n = n
        self.tree = [-inf] * (4*n)

    def update(self, i, val):
        def dfs(node, l, r):
            if l == r:
                self.tree[node] = max(self.tree[node], val)
                return
            m = (l+r)//2
            if i <= m:
                dfs(2*node, l, m)
            else:
                dfs(2*node+1, m+1, r)
            self.tree[node] = max(self.tree[2*node], self.tree[2*node+1])
        dfs(1, 0, self.n-1)

    def query(self, ql, qr):
        def dfs(node, l, r):
            if qr < l or ql > r:
                return -inf
            if ql <= l and r <= qr:
                return self.tree[node]
            m = (l+r)//2
            return max(dfs(2*node, l, m), dfs(2*node+1, m+1, r))
        return dfs(1, 0, self.n-1)

class Solution:
    def maxEarnings(self, meetings: list[list[int]]) -> int:
        meetings.sort(key = lambda x:x[0])
        n = len(meetings)
        
        unique = set()
        for l, r, c in meetings:
            unique.add(l)
            unique.add(r)
        lu = sorted(sorted(unique))
        corr = {lu[i]:i for i in range(len(lu))}
        st = SegTree(len(lu))

        dp = [0]*n
        dp[0] = meetings[0][2]
        st.update(corr[meetings[0][1]], dp[0]-meetings[0][1])

        for i in range(1, n):
            l, r, cost = meetings[i]
            cl, cr = corr[l], corr[r]
            dp[i] = max(st.query(0, cl) + l + cost, cost)
            st.update(cr, dp[i]-r)
        return max(dp)
                
