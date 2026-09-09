class Solution:
    def maxSubarrays(self, n: int, conflictingPairs: List[List[int]]) -> int:
        #1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15
        #[4, 8]
        tot = (n * (n+1)) // 2
        res = 0
        corr = {}
        for a, b in conflictingPairs:
            ntot = tot
            v1 = a-1
            v2 = n-b
            if v1 == 0 and v2 == 0:
                ntot = 0
            else:
                ntot -= max(v1, 1) * max(v2, 1)
            corr[(a, b)] = ntot
        print(corr)
