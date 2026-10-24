class SegTree:
    def __init__(self, nums):
        self.n = len(nums)
        self.tree = [0] * (4 * self.n)

        def build(node, l, r):
            if l == r:
                self.tree[node] = nums[l]
                return
            m = (l + r) // 2
            build(2 * node, l, m)
            build(2 * node + 1, m + 1, r)
            self.tree[node] = self.tree[2 * node] + self.tree[2 * node + 1]

        build(1, 0, self.n - 1)

    def update(self, i, val):
        def dfs(node, l, r):
            if l == r:
                self.tree[node] = val
                return
            m = (l + r) // 2
            if i <= m:
                dfs(2 * node, l, m)
            else:
                dfs(2 * node + 1, m + 1, r)
            self.tree[node] = self.tree[2 * node] + self.tree[2 * node + 1]

        dfs(1, 0, self.n - 1)

    def query(self, ql, qr):
        def dfs(node, l, r):
            if r < ql or l > qr:
                return 0
            if ql <= l and r <= qr:
                return self.tree[node]
            m = (l + r) // 2
            return dfs(2 * node, l, m) + dfs(2 * node + 1, m + 1, r)

        return dfs(1, 0, self.n - 1)


class Solution:
    def countOfPeaks(self, nums: list[int], queries: list[list[int]]) -> list[int]:
        n = len(nums)

        def calc(x):
            return x * (x - 1) // 2

        def peak(i):
            return 0 < i < n - 1 and nums[i] > nums[i - 1] and nums[i] > nums[i + 1]

        prev = [0] * n
        p = 0
        for i in range(n):
            prev[i] = p
            if peak(i):
                p = i

        nxt = [n - 1] * n
        p = n - 1
        for i in range(n - 1, -1, -1):
            nxt[i] = p
            if peak(i):
                p = i

        vals = [0] * n
        for i in range(1, n):
            if peak(i) or i == n - 1:
                vals[i] = calc(i - prev[i] + 1)

        st = SegTree(vals)

        def upd(idx, was, now):
            if was == now:
                return

            p, nx = prev[idx], nxt[idx]

            if was:
                nxt[p] = nx
                prev[nx] = p
                st.update(idx, 0)
                st.update(nx, calc(nx - prev[nx] + 1))
            else:
                nxt[p] = idx
                prev[idx] = p
                nxt[idx] = nx
                prev[nx] = idx
                st.update(idx, calc(idx - p + 1))
                st.update(nx, calc(nx - idx + 1))

        ans = []

        for q in queries:
            if q[0] == 1:
                l, r = q[1], q[2]
                bad = st.query(l, r)
                nv = nxt[l]
                pv = prev[r]
                bad -= l - prev[nv]
                bad += nxt[pv] - r
                ans.append(calc(r - l + 1) - bad)
            else:
                idx, val = q[1], q[2]

                affected = [i for i in (idx - 1, idx, idx + 1) if 0 < i < n - 1]
                old = {i: peak(i) for i in affected}

                nums[idx] = val

                new = {i: peak(i) for i in affected}

                for i in affected:
                    if old[i] and not new[i]:
                        upd(i, True, False)

                for i in affected:
                    if not old[i] and new[i]:
                        upd(i, False, True)

        return ans