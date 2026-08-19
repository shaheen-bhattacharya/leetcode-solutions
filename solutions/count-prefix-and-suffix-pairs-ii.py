class TrieNode:
    def __init__(self):
        self.children = {}
        self.isWord = False
        self.amt = 0
        self.count = 0
class Trie:
    def __init__(self):
        self.root = TrieNode()
        self.imap = {}

    def insert(self, word, idx):
        node = self.root
        prev = set()
        l, r = 0, len(word) - 1
        amt = 0
        while l < r:
            ch = (word[l], word[r])
            if ch not in node.children:
                node.children[ch] = TrieNode()
            node = node.children[ch]
            amt += node.count
            l += 1
            r -= 1

        node.isWord = True
        node.amt = amt
        self.imap[idx] = node.amt
        node.count += 1


class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        n = len(words)
        trie = Trie()
        for i, w in enumerate(words):
            trie.insert(w, i)

        res = 0
        print(trie.imap)

        for i in range(n):
            res += trie.imap[i]
        return res


                