class Solution:
    def resultArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = []
        ssl = SortedList([nums[0]])
        ssr = SortedList([nums[1]])
        
        for i in range(2, n):
            l = len(ssl) - ssl.bisect_right(nums[i])
            r = len(ssr) - ssr.bisect_right(nums[i])
            if l > r:
                ssl.add(nums[i])
            elif l < r:
                ssr.add(nums[i])
            else:
                ta = ssl if len(ssl) <= len(ssr) else ssr
                ta.add(nums[i])
        print(ssl, ssr)
        return list(ssl) + list(ssr)

