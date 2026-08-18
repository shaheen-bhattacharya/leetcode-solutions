class SegTree:
    def __init__(self, n):
        self.n = n
        self.tree = [0] * (4 * n)
    
    def update(self, i, val):
        def dfs(node, l, r):#node represents [l, r]
            if l == r and r == i:
                self.tree[node] = val
                return 
            mid = (l + r) // 2
            
            if i <= mid:
                dfs(2*node, l, mid)
            else:
                dfs(2*node+1, mid+1, r)

            self.tree[node] = max(self.tree[node*2], self.tree[2*node+1])
        return dfs(1, 0, self.n-1)

    def query(self, ql, qr):
        def dfs(node, l, r):
            if r < ql or l > qr:
                return 0
            
            if ql <= l and r <= qr:
                return self.tree[node]
            
            mid = (l + r) // 2
            return max(dfs(2*node, l, mid), dfs(2*node+1, mid+1, r))
        return dfs(1, 0, self.n-1)
    
class Solution:
    def getResults(self, queries: List[List[int]]) -> List[bool]:
        res = []
        obs = SortedList([0])
        n = max([q[1] for q in queries]) + 1
        seg = SegTree(n + 1)
        seg.update(0, inf)

        for q in queries:
            if q[0] == 1:
                if q[1] == 0:
                    continue
                idx = obs.bisect_left(q[1])
                prev = obs[idx - 1]
                nxt = obs[idx] if idx < len(obs) else -1
                seg.update(prev, q[1] - prev)
                if nxt == -1:
                    seg.update(q[1], inf)
                else:
                    seg.update(q[1], nxt - q[1])
                obs.add(q[1])
        
            else:
                res.append(q[2] <= seg.query(0, q[1]-q[2])) 
        return res
                

