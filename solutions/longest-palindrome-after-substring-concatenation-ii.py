class TrieNode:
    def __init__(self):
        self.isWord = False
        self.children = {}
        # Store a list of valid starting indices in reversed string 's'
        self.indices = []

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word, start_idx):
        node = self.root
        node.indices.append(start_idx)
        for ch in word:
            if ch not in node.children:
                node.children[ch] = TrieNode()
            node = node.children[ch]
            # Track all suffix starting positions passing through this prefix
            node.indices.append(start_idx)
        node.isWord = True

class Solution:
    def longestPalindrome(self, s: str, t: str) -> int:
        s_rev = s[::-1]
        
        def plen(word):
            n = len(word)
            best = [0] * (n + 1)
            for c in range(n):
                for l, r in [(c, c), (c, c + 1)]:
                    while l >= 0 and r < n and word[l] == word[r]:
                        best[l] = max(best[l], r - l + 1)
                        l -= 1
                        r += 1
            return best
        
        bestS = plen(s_rev)
        bestT = plen(t)

        trie = Trie()
        ns, nt = len(s_rev), len(t)
        
        for i in range(ns):
            trie.insert(s_rev[i:], i)    
            
        res = max(bestT[0], bestS[0])
        
        for i in range(nt):
            node = trie.root
            match_len = 0
            
            for j in range(i, nt):
                ch = t[j]
                if ch not in node.children:
                    break
                node = node.children[ch]
                match_len += 1
                
                # Check all starting positions in s_rev that share this matching prefix
                for s_start in node.indices:
                    s_rem_idx = s_start + match_len
                    t_rem_idx = j + 1
                    
                    s_pal = bestS[s_rem_idx] if s_rem_idx < ns else 0
                    t_pal = bestT[t_rem_idx] if t_rem_idx < nt else 0
                    
                    res = max(res, 2 * match_len + max(s_pal, t_pal))
                    
        return res