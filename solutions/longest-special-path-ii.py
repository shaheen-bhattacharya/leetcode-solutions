class Solution:
    def longestSpecialPath(self, edges: List[List[int]], nums: List[int]) -> List[int]:
        n = len(nums)
        adj = defaultdict(list)
        for u, v, l in edges:
            adj[u].append((v, l))
            adj[v].append((u, l))
        pref = [0] * n
        def pc(node, par):
            for nei, l in adj[node]:
                if nei == par:
                    continue
                pref[nei] = pref[node] + l
                pc(nei, node)

        pc(0, -1)

        best = 0
        mn = inf
        def dfs(node, par, occ, left, path):
            nonlocal best
            nonlocal mn
            nl = left
            val = nums[node]
            oldocc = occ[val][:]
            path.append(node)
            if len(occ[val]) == 2:
                if left < occ[val][-2]:
                    nl = occ[val][-2]
                    occ[val][-2] = occ[val][-1]
                    occ[val][-1] = len(path)-1
                else:
                    occ[val][-2] = occ[val][-1]
                    occ[val].pop()
                    if occ[val][-1] < left:
                        occ[val][-1].pop()
            else:
                occ[val].append(len(path)-1)
            tot = pref[node] - pref[path[nl]]
            if tot > best:
                best = tot
                mn = min(mn, len(path) - nl)
            
            for nei, l in adj[node]:
                if nei == par:
                    continue
                dfs(nei, node, occ, nl, path)
            path.pop()
            occ[val] = oldocc
        
        dfs(0, -1, defaultdict(list), 0, [])
        return [best, mn]


            
            

            
            

            




            





                    

                