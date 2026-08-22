class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        adj = defaultdict(set)
        n = len(tickets)
        for u, v in tickets:
            adj[u].add(v)

        res = []
        def dfs(node, adj, curr):
            nonlocal res
            # print(curr)
            if len(curr) == n+1:
                if res == []:
                    res = curr
                else:
                    res = min(res, curr)
                return 
            for nei in adj[node]:
                adj[node].remove(nei)
                curr.append(nei)
                dfs(nei, adj, curr)
                curr.pop()
                adj[node].add(nei)
        dfs("JFK", adj, [])
        return res
