class SegTree:
    def __init__(self, n):
        self.tree = [0] * (4*n)
        self.n = n
        self.lazy = [0] * (4*n)

    def push(self, node):
        if self.lazy[node] == 0:
            return
        val = self.lazy[node]
        left, right = 2*node, 2*node+1
        self.tree[left] = val
        self.tree[right] = val
        self.lazy[left] = val
        self.lazy[right] = val
        self.lazy[node] = 0


    def update(self, ql, qr, val):
        def dfs(node, l, r):
            if r < ql or l > qr:
                return 
            if ql <= l <= r <= qr:
                self.lazy[node] = val
                self.tree[node] = val
                return 
            self.push(node)
            m = (l+r)//2
            dfs(2*node, l, m)
            dfs(2*node+1, m+1, r)
            self.tree[node] = max(self.tree[2*node], self.tree[2*node+1])
        dfs(1, 0, self.n-1)

    def query(self, ql, qr):
        def dfs(node, l, r):
            if r < ql or l > qr:
                return 0
            if ql <= l <= r <= qr:
                return self.tree[node]
            m = (l+r)//2    
            self.push(node)
            return max(dfs(2*node, l, m), dfs(2*node+1, m+1, r))
        return dfs(1, 0, self.n-1)


class Solution:
    def fallingSquares(self, positions: list[list[int]]) -> list[int]:
        n = len(positions)
        res = []
        points = set()
        for l, d in positions:
            points.add(l)
            points.add(l+d)

        sp = list(sorted(points))
        corr = {sp[i]:i+1 for i in range(len(sp))}
        st = SegTree(len(sp)+2)

        for l, d in positions:
            r = l+d
            cl, cr = corr[l], corr[r]-1
            h = st.query(cl, cr)
            st.update(cl, cr, h+d)
            res.append(st.query(0, st.n-1))
        return res