class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        adj = defaultdict(set)
        n = len(tickets)
        for u, v in tickets:
            adj[u].add(v)

        adj["-1"] = {"JFK"}
        curr = []
        heap = [("JFK", "-1")]
        while heap:
            print(heap)
            node, par = heapq.heappop(heap)
            curr.append(node)   
            adj[par].discard(node)
            for nei in adj[node]:
                heapq.heappush(heap, (nei, node))
        return curr


