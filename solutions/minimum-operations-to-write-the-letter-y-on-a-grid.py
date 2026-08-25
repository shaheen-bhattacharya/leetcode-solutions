class Solution:
    def minimumOperationsToWriteY(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        fin = defaultdict(int)
        fout = defaultdict(int)

        for r in range(rows//2):
            for c in range(cols//2):
                if r == c:
                    fin[grid[r][c]] += 1
                else:
                    fout[grid[r][c]] += 1

        for r in range(rows//2):
            for c in range(cols-1, cols//2, -1):
                if cols - c - 1 == r:
                    fin[grid[r][c]] += 1
                else:
                    fout[grid[r][c]] += 1

        for r in range(rows//2, rows):
            for c in range(cols):
                if r == rows//2:
                    fin[grid[r][c]] += 1
                else:
                    fout[grid[r][c]] += 1
        print(fin)
        print(fout)
        res = inf
        res = min(res, fin[0] + fin[2] + fout[1] + fout[2], fin[0] + fin[2] + fout[0] + fout[1])
        res = min(res, fin[1] + fin[2] + fout[1] + fout[0], fin[1] + fin[2] + fout[0] + fout[2])
        res = min(res, fin[0] + fin[1] + fout[0] + fout[2], fin[0] + fin[1] + fout[1] + fout[2])
        return res


