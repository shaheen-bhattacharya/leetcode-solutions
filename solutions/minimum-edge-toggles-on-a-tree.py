class Solution:
    def minimumFlips(self, n: int, edges: List[List[int]], start: str, target: str) -> List[int]:
        adj = defaultdict(list)
        rev = {}
        for i, (u, v) in enumerate(edges):
            adj[u].append(v)
            adj[v].append(u)
            rev[(u, v)] = i
            rev[(v, u)] = i

        res = []
        solved = True
        def dfs(par, node):
            nonlocal solved
            if node != 0 and len(adj[node]) == 1:
                if start[node] != target[node]:
                    res.append(rev[(par, node)])
                    return True
                else:
                    return False
            count = 0
            for nei in adj[node]:
                if nei == par:
                    continue
                count += dfs(node, nei)

            if node == 0:
                if count % 2 != (start[node] == target[node]):
                    solved = False
                    return False
                else:
                    return True

            if count % 2 != (start[node] == target[node]):
                res.append(rev[(par, node)])
                return True
            else:
                return False

        dfs(-1, 0)
        res.sort()
        return res if solved else res
                
