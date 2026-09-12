class Solution:
    def braceExpansionII(self, expression: str) -> List[str]:
        #{a,b,c,d}{d,c,r,s,{ss,aa{ww}},f,x}{a,d,f,d,c}{d,f,d,c,g,r}
        #ab{}
        n = len(expression)
        def calc(ops):
            if len(ops) == 0:
                return set()
            if len(ops) == 1:
                return ops[0]
            ops = ops[::-1]
            while len(ops) > 1:
                st = set()
                fst = ops.pop()
                snd = ops.pop()
                for f in fst:
                    for s in snd:
                        st.add(f+s)
                ops.append(st)
            # print(ops[0])
            return ops[0]


        def dfs(l, r):
            if r < l:
                return set()
            # print(l, r)
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
                    if (l, r) == (1, 3):
                        print(need)
                    res |= calc(need)
                    need = []
                    i += 1
                if need:
                    res |= calc(need)
            # if (l, r) == (1, 3):
            #     print(res)
            return res

        return list(sorted(dfs(0, n-1)))






                