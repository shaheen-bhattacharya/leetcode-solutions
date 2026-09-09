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
        def dfs(node, par, occ, left, path, sml, sml2):
            nonlocal best
            nonlocal mn
            cl = left
            val = nums[node]
            path.append(node)
            occ[val].append(len(path) - 1)
            nsml = sml
            nsml2 = sml2
            k = len(occ[val])
            if k >= 3:
                cl = max(cl, occ[val][-3] + 1)

            if k >= 2:
                v = occ[val][-2] + 1
                if v > nsml:
                    nsml2 = nsml
                    nsml = v
                elif v > sml2:
                    nsml2 = v

            nl = max(left, nsml2)
            tot = pref[node] - pref[path[nl]]
            if tot > best:
                best = tot
                mn = min(mn, len(path) - nl)
            
            for nei, l in adj[node]:
                if nei == par:
                    continue
                dfs(nei, node, occ, cl, path, nsml, nsml2)

            path.pop()
            occ[val].pop()
        
        dfs(0, -1, defaultdict(list), 0, [], 0, 0)
        return [best, mn]


            
            

            
            

            




            





                    

                