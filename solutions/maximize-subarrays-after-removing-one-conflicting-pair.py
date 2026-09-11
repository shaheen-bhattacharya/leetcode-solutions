class Solution:
    def maxSubarrays(self, n: int, conflictingPairs: List[List[int]]) -> int:
        #1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15
        #[4, 8]
        
        pairs = defaultdict(list)
        for i, (a, b) in enumerate(conflictingPairs):
            if a > b:
                a, b = b, a
            pairs[b].append((a+1, i))
        
        mx1 = 1
        mx1id = 0
        mx2 = 1
        tot = 0
        gain = [0] * len(conflictingPairs)
        for i in range(1, n+1):
            for l, idx in pairs[i]:
                if l > mx1:
                    mx2 = mx1
                    mx1 = l
                    mx1id = idx
                elif l > mx2:
                    mx2 = l
            tot += i + 1 - mx1
            gain[mx1id] += mx1 - mx2
        return tot + max(gain)
            

                
        
        