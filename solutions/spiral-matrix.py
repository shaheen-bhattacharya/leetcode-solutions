class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        rows, cols = len(matrix), len(matrix[0])
        d = math.ceil(min(rows, cols) / 2)
        res = []
        print(d)
        for i in range(d):
            for c in range(d, cols-d):
                res.append(matrix[i][c])
            for r in range(d+1, rows-d-1):
                res.append(matrix[r][-i-1])
            for c in range(cols-d-1, d-1, -1):
                res.append(matrix[i][c])
            for r in range(rows-d-1, d, -1):
                res.append(matrix[r][i])
        return res