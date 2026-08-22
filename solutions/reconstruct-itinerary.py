class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        adj = defaultdict(list)
        n = len(tickets)
        for u, v in tickets:
            heapq.heappush(adj[u], v)

        res = []
        def dfs(node):
            while adj[node]:
                nei = heapq.heappop(adj[node])
                dfs(nei)
            res.append(node)
        dfs("JFK")
        return res[::-1]
        

