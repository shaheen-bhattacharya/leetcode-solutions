class TrieNode:
    def __init__(self):
        self.isWord = True
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
        trie = Trie()
        ns = len(s)
        nt = len(t)
        for i in range(ns):
            trie.insert(s[i:])    
        res = 0
        for i in range(nt):
            node = trie.root
            ch = t[i]
            cnt = 0
            while ch in node.children:
                cnt += 1
                node = node.children[ch]
            res = max(res, cnt)
        return res