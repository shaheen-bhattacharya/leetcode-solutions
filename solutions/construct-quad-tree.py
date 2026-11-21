"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""

class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':
        r = len(grid)
        def dfs(rl, cl, rr, cr):
            val = grid[rl][cl]
            flag = True
            for r in range(rl, rr+1):
                for c in range(cl, cr+1):
                    if grid[r][c] != val:
                        flag = False
                        break
            if flag:
                return Node(grid[rl][cl],True,None,None,None,None)

            rm = (rl+rr)//2
            cm = (cl+cr)//2
            # print(rl, cl, rr, cr, rm, cm)
            tl = dfs(rl, cl, rm, cm)
            tr = dfs(rl, cm+1, rm, cr)
            bl = dfs(rm+1, cl, rr, cm)
            br = dfs(rm+1, cm+1, rr, cr)
            return Node(-1, False, tl, tr, bl, br)

        return dfs(0,0,r-1,r-1)


