class TrieNode:
    def __init__(self):
        self.isWord = False
        self.children = {}
class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for i in range(len(word)-1, -1, -1):
            ch = word[i]
            if ch not in node.children:
                node.children[ch] = TrieNode()
            node = node.children[ch]
        node.isWord = True

class Solution:
    def longestPalindrome(self, s: str, t: str) -> int:
        #yrtxhrcbaterrt abcuitiutgu
        def lpal(word):
            nw = len(word)
            ret = 0
            for i in range(nw):
                for l, r in [(i, i), (i, i+1)]:
                    while l >= 0 and r < nw:
                        if word[l] == word[r]:
                            l -= 1
                            r += 1
                        else:
                            break
                    ret = max(ret, r - l - 1)
            return ret
                        
        trie = Trie()
        ns = len(s)
        nt = len(t)
        for i in range(ns):
            trie.insert(s[i:])    
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
            res = max(res, cnt)
        res = max(res, lpal(s), lpal(t))
        return res