class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        n = len(nums)
        l = 0
        res = 0
        freq = defaultdict(int)
        for r in range(n):
            freq[nums[r]] += 1
            curr = len(freq)
            while l <= r and curr > k:
                freq[nums[l]] -= 1
                if freq[nums[l]] == 0:
                    del freq[nums[l]]
                    curr -= 1
                l += 1

            tmp = defaultdict(int)
            tl = l
            while tl <= r:
                tmp[nums[tl]] += 1
                if tmp[nums[tl]] == freq[nums[tl]]:
                    break
                res += 1
                tl += 1
        return res
            
                
            


