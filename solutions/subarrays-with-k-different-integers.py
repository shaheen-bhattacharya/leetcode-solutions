class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        n = len(nums)
        l = 0
        res = 0
        freq = defaultdict(int)
        lidx = {}
        sl = SortedList()
        for r in range(n):
            freq[nums[r]] += 1
            if nums[r] not in lidx:
                sl.add(r)
            else:
                sl.discard(lidx[nums[r]])
                sl.add(r)
            lidx[nums[r]] = r

            curr = len(freq)
            while l <= r and curr > k:
                freq[nums[l]] -= 1
                if freq[nums[l]] == 0:
                    del freq[nums[l]]
                    sl.discard(lidx[nums[l]])
                    curr -= 1
                l += 1

            tmp = defaultdict(int)
            tl = l
            if curr == k:
                res += sl[0] - l + 1
        return res
            
                
            


