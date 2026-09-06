class TrieNode:
    def __init__(self):
        self.isWord = False
        self.children = {}
        self.idx = -1
class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word, idx):
        node = self.root
        for ch in word:
            if ch not in node.children:
                node.children[ch] = TrieNode()
            node.idx = idx
            idx += 1
            node = node.children[ch]
        node.isWord = True

class Solution:
    def longestPalindrome(self, s: str, t: str) -> int:
        #yrtxhrcbaterrt abcuitiutgu
        s = s[::-1]
        def plen(word):
            n = len(word)
            best = [1] * (n+1)
            for c in range(n):
                for l, r in [(c, c), (c, c+1)]:
                    while l >= 0 and r < n and word[l] == word[r]:
                        best[l] = max(best[l], r - l + 1)
                        l -= 1
                        r += 1
            best[-1] = 0
            return best
        
        bestS = plen(s)
        bestT = plen(t)
        
        trie = Trie()
        ns = len(s)
        nt = len(t)
        for i in range(ns):
            trie.insert(s[i:], i)    
        res = 0
        for i in range(nt):
            node = trie.root
            cnt = 0
            for j in range(i, nt):
                ch = t[j]
                if ch not in node.children:
                    break
                cnt += 2
                node = node.children[ch]
            print(cnt)
            sidx = node.idx+1
            print(bestS[sidx])
            tidx = j
            res = max(res, cnt + max(bestS[sidx], bestT[tidx]))
        return res