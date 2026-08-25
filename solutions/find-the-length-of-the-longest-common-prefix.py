class Solution:
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        sarr1 = [str(num) for num in arr1]
        sarr2 = [str(num) for num in arr2]
        pref1 = set()
        pref2 = set()

        for s1 in sarr1:
            for i in range(1, len(s1)+1):
                pref1.add(s1[:i])
        
        for s2 in sarr2:
            for i in range(1, len(s2)+1):
                pref2.add(s2[:i])
        res = 0
        for p1 in pref1:
            if p1 in pref2:
                res = max(res, len(p1))
        return res
        

