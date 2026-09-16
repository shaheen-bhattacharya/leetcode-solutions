class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        sarr = list(s)
        stack = []
        diff = 0
        for i, ch in enumerate(s):
            if ch == "(":
                diff += 1
                stack.append((ch, i))
            elif ch == ")":
                if diff == 0:
                    sarr[i] = ""
                    continue
                stack.append((ch, i))
                diff -= 1
        # print(diff)
        # print(stack)

        for i in range(len(sarr)-1, -1, -1):
            if diff == 0:
                break
            if sarr[i] == "(":
                sarr[i] = ""
                diff -= 1
            
        return "".join(sarr)
            

            