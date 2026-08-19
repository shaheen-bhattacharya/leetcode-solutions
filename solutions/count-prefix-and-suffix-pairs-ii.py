class TrieNode:
    def __init__(self):
        self.children = {}
        self.isWord = False
        self.idxs = set()
        self.prev = set()
class Trie:
    def __init__(self):
        self.root = TrieNode()
        self.imap = {}

    def insert(self, word, idx):
        node = self.root
        prev = set()
        for ch in word:
            if ch not in node.children:
                node.children[ch] = TrieNode()
            node = node.children[ch]
            if node.isWord:
                prev |= node.idxs

        node.isWord = True
        node.prev = prev
        node.idxs.add(idx)
        self.imap[idx] = prev 

class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        n = len(words)
        ftrie = Trie()
        btrie = Trie()
        for i, w in enumerate(words):
            ftrie.insert(w, i)
            btrie.insert(w[::-1], i)
        res = 0
        for i in range(n):
            nf = ftrie.imap[i]
            nb = btrie.imap[i]
            res += len(nf & nb)
            # nfp = nf.prev
            # nbp = nb.prev
            # comb = nbp & nfp
            # comb.discard(i)
            # res += len(comb)
            # print(i, nfp, nbp)            
        return res


                