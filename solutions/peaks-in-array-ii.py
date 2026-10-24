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
      if m >= i:
        dfs(2 * node, l, m)
      else:
        dfs(2 * node + 1, m + 1, r)
      self.tree[node] = self.tree[2 * node] + self.tree[2 * node + 1]

    dfs(1, 0, self.n - 1)

  def query(self, ql, qr):
    def dfs(node, l, r):
      if r < ql or l > qr:
        return 0
      if ql <= l <= r <= qr:
        return self.tree[node]
      m = (l + r) // 2
      return dfs(2 * node, l, m) + dfs(2 * node + 1, m + 1, r)

    return dfs(1, 0, self.n - 1)


class Solution:

  def countOfPeaks(
      self, nums: list[int], queries: list[list[int]]
  ) -> list[int]:
    n = len(nums)

    def calc(num):
      return int(num * (num - 1) / 2)

    def peak(i):
      if 0 < i < n - 1:
        return nums[i] > nums[i - 1] and nums[i] > nums[i + 1]
      return False

    peaks = SortedList()
    for i in range(1, n - 1):
      if peak(i):
        peaks.add(i)

    def get_prev(x):
      idx = peaks.bisect_left(x)
      return peaks[idx - 1] if idx > 0 else 0

    def get_nxt(x):
      idx = peaks.bisect_right(x)
      return peaks[idx] if idx < len(peaks) else n - 1

    vals = [0] * n
    for i in range(1, n - 1):
      if peak(i):
        vals[i] = calc(i - get_prev(i) + 1)
    vals[-1] = calc(n - 1 - get_prev(n - 1) + 1)

    res = []
    st = SegTree(vals)

    def upd(idx, wp, ip):
      if wp and not ip:
        nx_idx = peaks.bisect_right(idx)
        nx = peaks[nx_idx] if nx_idx < len(peaks) else n - 1
        peaks.remove(idx)
        st.update(idx, 0)
        if nx < n - 1:
          st.update(nx, calc(nx - get_prev(nx) + 1))
        st.update(n - 1, calc(n - 1 - get_prev(n - 1) + 1))
      elif not wp and ip:
        nx_idx = peaks.bisect_right(idx)
        nx = peaks[nx_idx] if nx_idx < len(peaks) else n - 1
        peaks.add(idx)
        st.update(idx, calc(idx - get_prev(idx) + 1))
        if nx < n - 1 and nx != idx:
          st.update(nx, calc(nx - get_prev(nx) + 1))
        st.update(n - 1, calc(n - 1 - get_prev(n - 1) + 1))

    for q in queries:
      if q[0] == 1:
        l, r = q[1], q[2]
        bad = st.query(l, r)

        idx_nv = peaks.bisect_left(l)
        nv = peaks[idx_nv] if idx_nv < len(peaks) else n - 1

        idx_pv = peaks.bisect_right(r) - 1
        pv = peaks[idx_pv] if 0 <= idx_pv < len(peaks) else 0

        bad -= l - get_prev(nv)
        bad += get_nxt(pv) - r
        res.append(calc(r - l + 1) - bad)
      else:
        idx, val = q[1], q[2]
        if idx == 0 or idx == n - 1:
          nums[idx] = val
          continue

        wpp, wpc, wpn = peak(idx - 1), peak(idx), peak(idx + 1)
        nums[idx] = val
        ipp, ipc, ipn = peak(idx - 1), peak(idx), peak(idx + 1)

        upd(idx - 1, wpp, ipp)
        upd(idx, wpc, ipc)
        upd(idx + 1, wpn, ipn)

    return res