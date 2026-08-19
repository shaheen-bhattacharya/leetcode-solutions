class Solution:
    def removeBoxes(self, boxes: List[int]) -> int:
        freq = Counter(boxes) 
        rev = defaultdict(int)
        for f in freq:
            rev[freq[f]] = f
        n = len(boxes)
        res = 0
        nb = []
        for f in range(1, 101):
            res += rev[f] * f**2
            del rev[f]
        return res
        
