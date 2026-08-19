class TrieNode:
    def __init__(self):
        self.children = {}
        self.isWord = False
        self.idx = -1
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
                prev.add(node.idx)

        node.isWord = True
        node.idx = idx
        node.prev = prev
        self.imap[idx] = node 

class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        # words.sort(key=len)
        # freq = Counter(words)
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
            nfp = nf.prev
            nbp = nb.prev
            print(i, nfp, nbp)
            # if len(nf) > len(nb):
            #     nf, nb = nb, nf 
            # for i in nfp:
            #     if i in nb:
            #         res += freq[words[i]]
        # for i in range()
            

        return res


                