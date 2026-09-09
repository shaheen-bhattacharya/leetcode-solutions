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
                    lazy[node] += val
                    tree[node] += val
                    return
                m = (l + r) //2
                push(node)
                dfs(2*node, l, m)
                dfs(2*node+1, m+1, r)
                tree[node] = max(tree[2*node], tree[2*node+1])
            dfs(1, 1, n-1)
        
        def sieve(n):
            primes = []
            lp = [-1] * (n+1)
            for i in range(2, n+1):
                if lp[i] == -1:
                    lp[i] = i
                    primes.append(i)
                for p in primes:
                    if p > lp[i] or p * i > n:
                        break
                    lp[p*i] = p
            return lp, primes

        lp, primes = sieve(max(nums))

        dist = 0
        for i, num in enumerate(nums):
            if lp[num] == num:
                if not pos[num]:
                    dist += 1
                if pos[num]:
                    pl, pr = pos[num][0], pos[num][-1]
                    update(pl+1, pr, -1)
                pos[num].add(i) 
                nl, nr = pos[num][0], pos[num][-1]
                update(nl+1, nr, 1)

        res = []
        for i, val in queries:
            old = nums[i]
            if lp[old] == old:
                pl, pr = pos[old][0], pos[old][-1]
                if pl < pr:
                    update(pl+1, pr, -1)
                pos[old].remove(i)
                if not pos[old]:
                    dist -= 1
            if lp[val] == val:
                if pos[val]:
                    plv, prv = pos[val][0], pos[val][-1]
                    if plv < prv:
                        update(plv, prv, -1)
                pos[val].add(i) 
                nl, nr = pos[val][0], pos[val][-1]
                update(nl+1, nr, 1)
                if len(pos[val]) == 1:      
                    dist += 1    
            nums[i] = val  
            res.append(dist + tree[1])
        return res

            

        
