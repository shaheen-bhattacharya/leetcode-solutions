class Solution:
    def countBlackBlocks(self, m: int, n: int, coordinates: List[List[int]]) -> List[int]:
        sc = set([tuple(c) for c in coordinates])
        res = [0] * 5
        tot = (m-1) * (n-1)
        starts = defaultdict(int)
        for r, c in coordinates:
            for dx, dy in [(0, 0), (0, -1), (-1, -1), (-1, 0)]:
                nr, nc = r + dx, c + dy
                if not (0 <= nr < m and 0 <= nc < n):
                    continue
                starts[(nr, nc)] += 1

        res[0] = tot
        for key in starts:
            res[starts[key]] += 1
            res[0] -= 1
        return res
                
