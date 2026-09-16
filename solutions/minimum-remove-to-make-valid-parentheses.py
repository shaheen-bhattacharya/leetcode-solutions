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
        print(diff)
        # print(stack)
        while stack and diff > 0:
            ch, i = stack.pop()
            if ch == "(":
                continue
            else:
                sarr[i] = ""
                diff -= 1
        for i in range(len(sarr)):
            if diff == 0:
                break
            if sarr[i] == "(":
                sarr[i] = ""
                diff -= 1
            
        return "".join(sarr)
            

            