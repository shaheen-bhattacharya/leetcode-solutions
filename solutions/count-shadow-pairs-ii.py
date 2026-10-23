class Solution:
    def shadowPairs(self, nums: list[int]) -> int:
        n = len(nums)
        res = n - 1
        gt = [0] * n
        sl = SortedList()
        for i in range(n-1, -1, -1):
            idx = sl.bisect_right(nums[i])
            gt[i] = len(sl) - idx
            sl.add(nums[i])
        print(gt)