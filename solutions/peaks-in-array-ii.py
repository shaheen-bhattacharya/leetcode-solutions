from sortedcontainers import SortedList

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

        def calc(num):
            return num * (num - 1) // 2

        def peak(i):
            return 0 < i < n - 1 and nums[i] > nums[i - 1] and nums[i] > nums[i + 1]

        # Keep your sentinel-based representation.
        peaks = SortedList([0] + [i for i in range(1, n - 1) if peak(i)] + [n - 1])

        vals = [0] * n

        for j in range(1, len(peaks)):
            p = peaks[j]
            prev_p = peaks[j - 1]
            vals[p] = calc(p - prev_p + 1)

        st = SegTree(vals)
        res = []

        def upd(idx, was, now):
            if was == now or idx == 0 or idx == n - 1:
                return

            if was:
                j = peaks.bisect_left(idx)
                p, nx = peaks[j - 1], peaks[j + 1]

                # Remove idx's contribution.
                st.update(idx, 0)

                # Successor now uses p as its previous peak.
                st.update(nx, calc(nx - p + 1))
                peaks.remove(idx)

            else:
                j = peaks.bisect_left(idx)
                p, nx = peaks[j - 1], peaks[j]

                # Insert idx between p and nx.
                peaks.add(idx)

                st.update(idx, calc(idx - p + 1))
                st.update(nx, calc(nx - idx + 1))

        for q in queries:
            if q[0] == 1:
                l, r = q[1], q[2]

                first = peaks.bisect_right(l)
                last = peaks.bisect_left(r) - 1

                if first > last:
                    res.append(0)
                    continue

                # Preserve your original query formula.
                a = peaks[first]
                b = peaks[last]

                bad = st.query(a, b)
                bad -= calc(a - l + 1)
                bad -= calc(r - b + 1)

                res.append(calc(r - l + 1) - bad)

            else:
                idx, val = q[1], q[2]

                affected = [i for i in (idx - 1, idx, idx + 1) if 0 < i < n - 1]
                old = {i: peak(i) for i in affected}

                nums[idx] = val

                new = {i: peak(i) for i in affected}

                # Remove old peaks first, then insert newly created peaks.
                for i in affected:
                    if old[i] and not new[i]:
                        upd(i, True, False)

                for i in affected:
                    if not old[i] and new[i]:
                        upd(i, False, True)

        return res