from collections import defaultdict
from typing import List

class Solution:
    def longestSpecialPath(self, edges: List[List[int]], nums: List[int]) -> List[int]:
        n = len(nums)
        adj = defaultdict(list)
        for u, v, l in edges:
            adj[u].append((v, l))
            adj[v].append((u, l))
            
        best_len = 0
        min_nodes = 1
        
        # Maps value -> list of depth indices where it appears along current path
        occ = defaultdict(list)
        
        # Prefix distances from root to current depth
        pref = [0]
        
        def dfs(node, par, hard_left, depth, dup_bounds):
            nonlocal best_len, min_nodes
            
            val = nums[node]
            occ[val].append(depth)
            k = len(occ[val])
            
            # Rule 1: NO value can appear 3 or more times.
            # If val appears 3+ times, the path CANNOT include the 1st occurrence (depth occ[val][-3]).
            # Thus, hard_left must be pushed past occ[val][-3].
            if k >= 3:
                hard_left = max(hard_left, occ[val][-3] + 1)
                
            # Rule 2: Collect duplicate boundary constraints.
            # A duplicate pair occurs when k >= 2 at indices (occ[val][-2], depth).
            # To eliminate this duplicate pair, L would need to be >= occ[val][-2] + 1.
            new_dup_bounds = list(dup_bounds)
            if k >= 2:
                bound = occ[val][-2] + 1
                new_dup_bounds.append(bound)
                new_dup_bounds.sort()
                
            # Rule 3: Allow AT MOST ONE duplicate pair on the path.
            # If we have 2 or more duplicate pairs active, we MUST eliminate all but 1.
            # Thus, effective_left must be at least the 2nd largest duplicate boundary.
            effective_left = hard_left
            if len(new_dup_bounds) >= 2:
                effective_left = max(effective_left, new_dup_bounds[-2])

            # Calculate current path length and node count
            path_len = pref[depth] - pref[effective_left]
            node_cnt = depth - effective_left + 1
            
            if path_len > best_len:
                best_len = path_len
                min_nodes = node_cnt
            elif path_len == best_len:
                min_nodes = min(min_nodes, node_cnt)
                
            # Recursively traverse children
            for nei, w in adj[node]:
                if nei == par:
                    continue
                pref.append(pref[-1] + w)
                dfs(nei, node, hard_left, depth + 1, new_dup_bounds)
                pref.pop()
                
            # Backtrack state
            occ[val].pop()

        dfs(0, -1, 0, 0, [])
        return [best_len, min_nodes]