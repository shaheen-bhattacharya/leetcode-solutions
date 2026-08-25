class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        rows, cols = len(matrix), len(matrix[0])
        d = math.ceil(min(rows, cols) / 2)
        res = []
        for i in range(d):
            for c in range(i, cols-i):
                res.append(matrix[i][c])
            for r in range(i+1, rows-i-1):
                res.append(matrix[r][-i-1])
            for c in range(cols-i-1, i-1, -1):
                res.append(matrix[-i-1][c])
            for r in range(rows-i-1, i, -1):
                res.append(matrix[r][i])
        return res