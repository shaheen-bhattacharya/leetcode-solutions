from sortedcontainers import SortedList

class FenwickTree:
    def __init__(self, n):
        self.n = n
        self.bit = [0] * (n + 1)

    def update(self, i, delta):
        i += 1
        while i <= self.n:
            self.bit[i] += delta
            i += i & -i

    def query(self, i):
        # Sum over indices [0, i)
        res = 0
        while i > 0:
            res += self.bit[i]
            i -= i & -i
        return res

    def range_sum(self, l, r):
        # Inclusive range [l, r]
        return self.query(r + 1) - self.query(l)


class Solution:
    def countOfPeaks(self, nums: list[int], queries: list[list[int]]) -> list[int]:
        n = len(nums)

        def is_peak(i):
            return (
                0 < i < n - 1
                and nums[i] > nums[i - 1]
                and nums[i] > nums[i + 1]
            )

        peaks = SortedList(i for i in range(1, n - 1) if is_peak(i))
        bit = FenwickTree(n)

        def weight(p, prev):
            return p * (p - prev)

        # Initialize weighted contributions.
        prev = 0
        for p in peaks:
            bit.update(p, weight(p, prev))
            prev = p

        def insert_peak(p):
            j = peaks.bisect_left(p)
            prev = peaks[j - 1] if j > 0 else 0
            nxt = peaks[j] if j < len(peaks) else None

            # The successor's previous peak changes from prev to p.
            if nxt is not None:
                bit.update(nxt, weight(nxt, p) - weight(nxt, prev))

            bit.update(p, weight(p, prev))
            peaks.add(p)

        def remove_peak(p):
            j = peaks.bisect_left(p)
            prev = peaks[j - 1] if j > 0 else 0
            nxt = peaks[j + 1] if j + 1 < len(peaks) else None

            bit.update(p, -weight(p, prev))

            # The successor's previous peak changes from p to prev.
            if nxt is not None:
                bit.update(nxt, weight(nxt, prev) - weight(nxt, p))

            peaks.remove(p)

        ans = []

        for typ, x, y in queries:
            if typ == 1:
                l, r = x, y

                left = peaks.bisect_right(l)
                right = peaks.bisect_left(r) - 1

                if left > right:
                    ans.append(0)
                    continue

                a = peaks[left]
                b = peaks[right]
                prev = peaks[left - 1] if left > 0 else 0

                # Sum of p * (p - previous_peak) for peaks in [a, b].
                W = bit.range_sum(a, b)

                ans.append(r * (b - l) - W + a * (l - prev))

            else:
                idx, val = x, y

                # Only these three positions can change peak status.
                affected = [
                    i for i in (idx - 1, idx, idx + 1)
                    if 0 < i < n - 1
                ]

                # Remove old peaks before changing nums.
                for i in affected:
                    if is_peak(i):
                        remove_peak(i)

                nums[idx] = val

                # Reinsert positions that are peaks after the update.
                for i in affected:
                    if is_peak(i):
                        insert_peak(i)

        return ans