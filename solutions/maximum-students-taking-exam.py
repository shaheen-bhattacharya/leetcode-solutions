class Solution:
    def maxStudents(self, seats: list[list[str]]) -> int:
        adj = defaultdict(list)
        rows, cols = len(seats), len(seats[0])
        directions = [(0, -1), (0, 1), (-1, -1), (-1, 1)]
        good = 0
        for r in range(rows):
            for c in range(cols):
                if seats[r][c] != "." and (r+c)%2==0:
                    continue
                good += 1
                for dx, dy in directions:
                    nr, nc = r + dx, c + dy
                    if not (0 <= nr < rows and 0 <= nc < cols):
                        continue
                    if seats[nr][nc] == ".":
                        adj[(r, c)].append((nr, nc))

        match = [[(-1, -1)]*cols for _ in range(rows)]

        def dfs(r, c, seen):
            for nr, nc in adj[(r, c)]:
                if seen[nr][nc]:
                    continue
                mr, mc = match[nr][nc]
                seen[nr][nc] = True
                if match[nr][nc] == (-1, -1) or dfs(mr, mc, seen):
                    match[nr][nc] = (mr, mc)
                    return True
            return False

        res = 0
        for r in range(rows):
            for c in range(cols):
                seen = [[False]*cols for _ in range(rows)]
                if dfs(r, c, seen):
                    res += 1    
        return good - res
                    

                    