class Solution:
    def countGoodIntegersOnPath(self, l: int, r: int, directions: str) -> int:
        idxs = [0] * 7
        r, c = 0,0
        for i in range(1, 7):
            if directions[i-1] == "D":
                r += 1
            else:
                c += 1
            idxs[i] = r*4+c
        print(idxs)
