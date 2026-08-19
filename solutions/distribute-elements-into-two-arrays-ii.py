class Solution:
    def resultArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        a1 = []
        a2 = []

        ssl = SortedList([nums[0]])
        ssr = SortedList([nums[1]])
        
        for i in range(2, n):
            l = len(ssl) - ssl.bisect_right(nums[i])
            r = len(ssr) - ssr.bisect_right(nums[i])
            if l > r:
                a1.append(nums[i])
                ssl.add(nums[i])
            elif l < r:
                a2.append(nums[i])
                ssr.add(nums[i])
            else:
                ta = ssl if len(ssl) <= len(ssr) else ssr
                tb = a1 if len(ssl) <= len(ssr) else a2
                ta.add(nums[i])
                tb.append(nums[i])
        # print(ssl, ssr)
        return a1 + a2

