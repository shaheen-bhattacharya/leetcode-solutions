class Solution:
    def maximumCount(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        n = len(nums)
        tree = [0] * (4 * n)
        lazy = [0] * (4 * n)
        pos = [SortedList() for _ in range(100001)]

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
                if ql <= m:
                    dfs(2*node, l, m)
                if qr > m:
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

        lp, primes = sieve(100001)

        dist = 0
        for i, num in enumerate(nums):
            if lp[num] == num:
                pos[num].add(i) 
                if len(pos[num]) == 1:
                    dist += 1
        
        for num in range(2, 100001):
            if pos[num]:
                l, r = pos[num][0], pos[num][-1]
                if l < r:
                    update(l+1, r, 1)

        res = []
        for i, val in queries:
            old = nums[i]
            if lp[old] == old:
                pl, pr = pos[old][0], pos[old][-1]
                pos[old].remove(i)
                if pos[old]:
                    nl, nr = pos[old][0], pos[old][-1]
                    if nl > pl:
                        update(pl+1, nl, -1)
                    if nr < pr:
                        update(nr+1, pr, -1)
                else:
                    if pl < pr:
                        update(pl+1, pr, -1)
                    dist -= 1

            if lp[val] == val:
                if not pos[val]:
                    dist += 1
                    pos[val].add(i)
                else:
                    plv, prv = pos[val][0], pos[val][-1]
                    pos[val].add(i) 
                    nl, nr = pos[val][0], pos[val][-1]
                    if nl < plv:
                        update(nl+1, plv, 1)
                    if nr > prv:
                        update(prv+1, nr, 1)

            nums[i] = val  
            res.append(dist + tree[1])
        return res

            

        
