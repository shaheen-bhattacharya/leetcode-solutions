class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        n = len(nums)
        l = 0
        l2 = 0
        res = 0
        freq = defaultdict(int)
        freq2 = defaultdict(int)

        for r in range(n):
            freq[nums[r]] += 1
            freq2[nums[r]] += 1

            curr = len(freq)
            curr2 = len(freq2)
            # print(freq)
            while l2 <= r and l <= r and curr > k and curr2 >= k:
                if curr > k:
                    freq[nums[l]] -= 1
                    freq2[nums[l2]] -= 1
                    if freq[nums[l2]] == 0:
                        del freq[nums[l2]]
                        curr2 -= 1
                    if freq[nums[l]] == 0:
                        del freq[nums[l]]
                        curr -= 1
                    l += 1
                    l2 += 1
                else:
                    freq2[nums[l2]] -= 1
                    if freq[nums[l2]] == 0:
                        del freq[nums[l2]]
                        curr2 -= 1
                    l2 += 1
            print(l, l2)
            if curr == k:
                res += l2 - l + 1
        return res
            
                
            


