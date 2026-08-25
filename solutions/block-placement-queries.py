class Solution:
    def getResults(self, queries: List[List[int]]) -> List[bool]:
        inf = 10**10
        n = max(q[1] for q in queries)
        tree = [0] * (4 * (n+1))
        #tree[node] = max pos from [l, r) where 
        def update(idx, amt):
            def dfs(node, l, r):
                if l+1 == r:
                    tree[node] = amt
                    return 
                m = (l + r) // 2
                if m > idx:
                    dfs(2 * node, l, m)
                else:
                    dfs(2 * node + 1, m, r)
                tree[node] = max(tree[2 * node], tree[2*node+1])
            dfs(1, 0, n)

        def query(ql, qr):
            def dfs(node, l, r):
                if ql >= r or qr <= l:
                    return 0
                if ql <= l and r <= qr:
                    return tree[node]
                m = (l + r) // 2
                return max(dfs(2 * node, l, m), dfs(2 * node + 1, m, r))
            return dfs(1, 0, n)

        sl = SortedList([0])
        # update(0, inf)
        res = []
        for i in range(len(queries)):
            if queries[i][0] == 1:
                x = queries[i][1]
                sl.add(x)
                i = sl.bisect_left(x)
                if i + 1 == len(sl):
                    update(x, inf)
                else:
                    update(x, sl[i+1] - x)
                update(sl[i-1], x - sl[i-1])
            else:
                x, sz = queries[i][1], queries[i][2]
                res.append(query(0, x-sz) >= sz)
        return res
                



