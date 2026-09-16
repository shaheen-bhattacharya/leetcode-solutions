class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        sarr = list(s)
        diff = 0
        for i, ch in enumerate(s):
            if ch == "(":
                diff += 1
            elif ch == ")":
                if diff == 0:
                    sarr[i] = ""
                    continue
                diff -= 1

        for i in range(len(sarr)-1, -1, -1):
            if diff == 0:
                break
            if sarr[i] == "(":
                sarr[i] = ""
                diff -= 1
            
        return "".join(sarr)
            

            