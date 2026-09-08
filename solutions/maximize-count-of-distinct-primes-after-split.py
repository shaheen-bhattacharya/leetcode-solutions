class Solution:
    def maximumCount(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        n = len(nums)
        tree = [0] * (4 * n)
        lazy = [0] * (4 * n)
        maxv = max(nums)
        pos = defaultdict(SortedList)

        def push(node):
            if lazy[node] != 0:
                tree[2*node] += lazy[node]
                tree[2*node+1] += lazy[node]
                lazy[2*node] += lazy[node]
                lazy[2*node+1] += lazy[node]
                lazy[node] = 0

        def update(ql, qr, val):
            def dfs(node, l, r):
                if r < ql or l > qr:
                    return 
                if ql <= l and r <= qr:
                    lazy[node] += 1
                    tree[node] += 1
                    return
                m = (l + r) //2
                push(node)
                dfs(2*node, l, m)
                dfs(2*node+1, m+1, r)
                tree[node] = max(tree[2*node], tree[2*node+1])
            dfs(1, 1, n)
        
        def query(ql, qr):
            def dfs(node, l, r):
                if r < ql or l > qr:
                    return 0
                if ql <= l and r <= qr:
                    return tree[node]
                m = (l+r)//2
                push(node)
                return max(dfs(2*node, l, m), dfs(2*node+1, m+1, r))
            return dfs(1, 1, n)

        for i, num in enumerate(nums):
            pos[num].add(i)

        res = []
        for i, val in queries:
            old = nums[i]
            pl, pr = pos[old][0], pos[old][-1]
            pos[old].remove(i)
            nums[i] = val
            pos[val].add(i)
            nl, nr = pos[val][0], pos[val][-1]
            if nl < pl:
                update(nl+1, min(pl, nr), val)
            elif nr > pr:
                update(max(nl, pr)+1, nr, val)
            res.append(query(1, n))
        return res

            

        
