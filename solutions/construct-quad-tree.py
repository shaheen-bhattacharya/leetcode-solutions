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
            if rl == rr and cr == cl:
                return Node(grid[rl][cl],True,None,None,None,None)
            rm = (rl+rr)//2
            cm = (cl+cr)//2
            # print(rl, cl, rr, cr, rm, cm)
            tl = dfs(rl, cl, rm, cm)
            tr = dfs(rl, cm+1, rm, cr)
            bl = dfs(rm+1, cl, rr, cm)
            br = dfs(rm+1, cm+1, rr, cr)
            ret = Node()
            if (not (tl.val == tr.val == bl.val == br.val)) and tl.val != -1:
                ret.val = tl.val
                ret.isLeaf = True
            else:
                ret.val = tl.val
                ret.isLeaf = True
            ret.topLeft = tl
            ret.topRight = tr
            ret.bottomRight = br
            ret.bottomLeft = bl
            return ret
        return dfs(0,0,r-1,r-1)


