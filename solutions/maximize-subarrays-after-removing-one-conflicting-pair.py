class Solution:
    def maxSubarrays(self, n: int, conflictingPairs: List[List[int]]) -> int:
        #1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15
        #[4, 8]

        fst = [1] * (n+1)
        snd = [1] * (n+1)
        
        pairs = defaultdict(list)
        for i, (a, b) in enumerate(conflictingPairs):
            if a > b:
                a, b = b, a
            pairs[b].append(a+1)
        
        mx1 = 1
        mx2 = 1
        tot = 0
        for i in range(1, n+1):
            for l in pairs[i]:
                if l > mx1:
                    mx2 = mx1
                    mx1 = l
                elif l > mx2:
                    mx2 = l
            fst[i] = mx1
            snd[i] = mx2
            tot += fst[i] - i + 1
        
        res = 0
        for a, b in conflictingPairs:
            if a > b:
                a, b = b, a
            nl = fst[b] - b + 1
            ntot = tot - nl
            if a+1 == fst[b]:
                nl = snd[b] - b + 1
            ntot += nl
            res = max(res, ntot)
        return res


                
        
        