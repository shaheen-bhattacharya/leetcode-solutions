class SegTree:
    def __init__(self, nums):
        self.n = len(nums)
        self.tree = [0] * (4*self.n)
        def build(node, l, r):
            if l == r:
                self.tree[node] = nums[l]
                return 
            m = (l+r)//2
            build(2*node, l, m)
            build(2*node+1, m+1, r) 
            self.tree[node] = self.tree[2*node] + self.tree[2*node+1]
        build(1, 0, self.n-1)

    def update(self, i, val):
        def dfs(node, l, r):
            if l == r:
                self.tree[node] = val
                return 
            m = (l+r)//2
            if m >= i:
                dfs(2*node, l, m)
            else:
                dfs(2*node+1, m+1, r)
            self.tree[node] = self.tree[2*node] + self.tree[2*node+1]
        dfs(1, 0, self.n-1)
    
    def query(self, ql, qr):
        def dfs(node, l, r):
            if r < ql or l > qr:
                return 0
            if ql <= l <= r <= qr:
                return self.tree[node]
            m = (l+r)//2
            return dfs(2*node, l, m) + dfs(2*node+1, m+1, r)
        return dfs(1, 0, self.n-1)

class Solution:
    def countOfPeaks(self, nums: list[int], queries: list[list[int]]) -> list[int]:
        n = len(nums)
        """
        .|....|...|....|.....|....|.
        """
        def calc(num):
            return int(num * (num-1)/2)
        def peak(i):
            if i == 0:
                return False
            if i == n-1:
                return True
            return nums[i] > nums[i-1] and nums[i] > nums[i+1]

        prev = [0] * n
        pp = 0
        for i in range(n):
            prev[i] = pp
            if (1 <= i <= n-2) and nums[i] > nums[i-1] and nums[i] > nums[i+1]:
                pp = i
        
        nxt = [0] * n
        np = n-1
        for i in range(n-1, -1, -1):
            nxt[i] = np
            if (1 <= i <= n-2) and nums[i] > nums[i-1] and nums[i] > nums[i+1]:
                np = i

        vals = [0] * n
        for i in range(1, n-1):
            amt = i - prev[i] + 1
            if nums[i] > nums[i-1] and nums[i] > nums[i+1]:
                vals[i] = calc(amt)

        vals[-1] = calc(n-1-prev[n-1]+1)
        
        print(prev)
        print(nxt)
        print("\n")
        res = []
        st = SegTree(vals)

        def upd(idx, wp, ip):
            if wp and not ip:
                st.update(idx, 0)
                st.update(nxt[idx], nxt[idx]-prev[idx]+1)
                nxt[prev[idx]] = nxt[idx]
                prev[nxt[idx]] = prev[idx]
            elif not wp and ip:
                st.update(idx, calc(idx-prev[idx]+1))
                st.update(nxt[idx], calc(nxt[idx]-idx+1))
                nxt[prev[idx]] = idx
                prev[nxt[idx]] = idx

        for q in queries:
            if q[0] == 1:
                l, r = q[1], q[2]
                bad = st.query(l, r)
                nv = nxt[l]
                pv = prev[r]
                bad -= l - prev[nv]
                bad += nxt[pv] - r
                res.append(calc(r-l+1)-bad)
            else:
                idx, val = q[1], q[2]
                if idx == 0 or idx == n-1:
                    nums[idx] = val
                    continue
                
                wpp, wpc, wpn = peak(idx-1), peak(idx), peak(idx+1)
                nums[idx] = val
                ipp, ipc, ipn = peak(idx-1), peak(idx), peak(idx+1)

                upd(idx-1, wpp, ipp)
                upd(idx, wpc, ipc)
                upd(idx+1, wpn, ipn)

                print(prev)
                print(nxt)
        return res





