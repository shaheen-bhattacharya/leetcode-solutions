class Solution:
    def maxSubarrays(self, n: int, conflictingPairs: List[List[int]]) -> int:
        #1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15
        #[4, 8]

        fst = [0] * (n+1) #fst[i] = earlierst l pos for l to i be valid 
        snd = [0] * (n+1)

        for a, b in conflictingPairs:
            if a > b:
                a, b = b, a
            if a + 1 > fst[b]:
                snd[b] = fst[b]
                fst[b] = a+1
            elif a+1 > snd[b]:
                snd[b] = a+1
        tot = 0
        for i in range(1, n+1):
            l = fst[i] - i + 1
            tot += (l * (l+1))//2

        res = 0
        for a, b in conflictingPairs:
            if a > b:
                a, b = b, a
            pl = fst[b] - b + 1
            ntot = tot - (pl * (pl+1))//2
            nl = fst[b] - b + 1
            if fst[b] == a + 1:
                nl = snd[b] - b + 1
            ntot += (nl * (nl+1))//2
            res = max(res, ntot)
        return res
                

