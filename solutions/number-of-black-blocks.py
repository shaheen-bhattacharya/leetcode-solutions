class Solution:
    def countBlackBlocks(self, m: int, n: int, coordinates: List[List[int]]) -> List[int]:
        sc = set([tuple(c) for c in coordinates])
        res = [0] * 5
        for r in range(m-1):
            for c in range(n - 1):
                bc = 0
                for dx, dy in [(0, 1), (0, 0), (1, 0), (1, 1)]:
                    nr, nc = r + dx, c + dy
                    if (nr, nc) in sc:
                        bc += 1
                res[bc] += 1
        return res
                
