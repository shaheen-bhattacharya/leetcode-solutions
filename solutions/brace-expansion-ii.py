class Solution:
    def braceExpansionII(self, expression: str) -> List[str]:
        #{a,b,c,d}{d,c,r,s,{ss,aa{ww}},f,x}{a,d,f,d,c}{d,f,d,c,g,r}
        #ab{}
        n = len(expression)
        def calc(ops):
            st = set()
            ops = ops[::-1]
            while len(ops) > 1:
                fst = ops.pop()
                snd = ops.pop()
                for f in fst:
                    for s in snd:
                        st.add(f+s)
            return st

        def dfs(l, r):
            if r < l:
                return set()
            print(l, r)
            res = set()
            need = []
            i = l
            while i <= r:
                if expression[i].isalpha():
                    need.append(set([expression[i]]))
                    i += 1
                elif expression[i] == "{":
                    tmp = 1
                    s = i
                    i += 1
                    while i <= r and tmp != 0:
                        if expression[i] == "{":
                            tmp += 1
                        elif expression[i] == "}":
                            tmp -= 1
                        i += 1
                    need.append(dfs(s+1, i-2))
                    end = False
                else:
                    res |= calc(need)
                    need = []
                    i += 1
                return res

        return list(sorted(dfs(0, n-1)))






                