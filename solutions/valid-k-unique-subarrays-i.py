class SD:
    def __init__(self, nums):
        self.freq = {}
        self.nums = nums
        self.n = len(nums)
        self.B = max(1, isqrt(self.n))
        self.blocks = [0] * ((self.n + self.B - 1) // self.B)
        self.odds = 0

        for i, x in enumerate(nums):
            b = i//self.B
            old = self.freq[nums[i]] if nums[i] in self.freq else 0
            if nums[i] not in self.freq:
                self.freq[nums[i]] = 0
                self.blocks[b] += 1
            self.freq[nums[i]] += 1

    def add(self, i):
        b = i//self.B
        old = self.freq[self.nums[i]] if self.nums[i] in self.freq else 0
        if self.nums[i] not in self.freq:
            self.freq[self.nums[i]] = 0
            self.blocks[b] += 1
        self.freq[self.nums[i]] += 1

        if old % 2 == 1:
            self.odds -= 1
        elif old != 0:
            self.odds += 1

    def delete(self, i):
        b = i//self.B
        old = self.freq[self.nums[i]] 
        self.freq[self.nums[i]] -= 1
        if self.freq[self.nums[i]] == 0:
            del self.freq[self.nums[i]]
            self.blocks[b] -= 1
        if old % 2 == 0:
            self.odds += 1
        elif old != 0:
            self.odds -= 1

class Solution:
    def validSubarrays(self, nums: list[int], k: int, queries: list[list[int]]) -> list[bool]:      
        n = len(nums)
        maxv = max(nums)
        sd = SD(nums)
        qs = [(q, i) for i, q in enumerate(queries)]
        qs.sort(key=lambda x: (x[0][0]//sd.B, x[0][1]))
        freq = defaultdict(int)
        odds = set()
        L, R = 0, -1
        res = [False]*n
        for (l, r), i in qs:
            while L > l:
                sd.delete(L)
                L -= 1
            while R > r:
                sd.delete(R)
                R -= 1
            while L < l:
                sd.add(L)
                L += 1
            while R < r:
                sd.add(R)
                R += 1
            res[i] = (len(sd.freq) == k and sd.odds == 0)
        return res
