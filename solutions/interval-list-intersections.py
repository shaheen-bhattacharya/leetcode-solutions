class Solution:
    def intervalIntersection(self, firstList: list[list[int]], secondList: list[list[int]]) -> list[list[int]]:
        fp = 0
        sp = 0
        res = []
        while fp < len(firstList) and sp < len(secondList):
            fs, fe = firstList[fp]
            ss, se = secondList[sp]
            s, e = max(fs, ss), min(fe, se)
            if s <= e:
                res.append([s, e])
            if fe <= se:
                fp += 1
            else:
                sp += 1
        return res                    



