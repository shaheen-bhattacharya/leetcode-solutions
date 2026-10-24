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
    peaks = SortedList()

    def peak(i):
      if 0 < i < n - 1:
        return nums[i] > nums[i - 1] and nums[i] > nums[i + 1]
      return False

    def get_val(p):
      idx = peaks.bisect_left(p)
      prev_p = peaks[idx - 1] if idx > 0 else 0
      return p * (p - prev_p)

    for i in range(1, n - 1):
      if peak(i):
        peaks.add(i)

    vals = [0] * n
    for p in peaks:
      vals[p] = get_val(p)

    st = SegTree(vals)

    def add_peak(p):
      peaks.add(p)
      st.update(p, get_val(p))
      nx_idx = peaks.bisect_right(p)
      if nx_idx < len(peaks):
        nx = peaks[nx_idx]
        st.update(nx, get_val(nx))

    def remove_peak(p):
      nx_idx = peaks.bisect_right(p)
      nx = peaks[nx_idx] if nx_idx < len(peaks) else -1
      peaks.remove(p)
      st.update(p, 0)
      if nx != -1:
        st.update(nx, get_val(nx))

    res = []
    for q in queries:
      if q[0] == 1:
        l, r = q[1], q[2]
        left_bound = l + 1
        right_bound = r - 1
        if left_bound > right_bound:
          res.append(0)
          continue

        idx_a = peaks.bisect_left(left_bound)
        idx_b = peaks.bisect_right(right_bound) - 1

        if idx_a > idx_b or idx_a >= len(peaks) or idx_b < 0:
          res.append(0)
          continue

        a = peaks[idx_a]
        b = peaks[idx_b]
        if a > right_bound or b < left_bound:
          res.append(0)
          continue

        pos_a = peaks.bisect_left(a)
        q_val = peaks[pos_a - 1] if pos_a > 0 else 0

        W = st.query(a, b)
        ans = r * (b - l) - W + a * (l - q_val)
        res.append(ans)
      else:
        idx, val = q[1], q[2]
        nums[idx] = val

        for i in range(idx - 1, idx + 2):
          if 0 < i < n - 1:
            was_p = i in peaks
            is_p = peak(i)
            if was_p and not is_p:
              remove_peak(i)
            elif not was_p and is_p:
              add_peak(i)

    return res