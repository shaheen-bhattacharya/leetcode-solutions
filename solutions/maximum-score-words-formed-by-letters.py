class TrieNode:
    def __init__(self):
        self.ch = {}
        self.isWord = False
class Trie:
    def __init__(self):
        self.root = TrieNode()
    def insert(self, word):
        node = self.root
        for ch in word:
            if ch not in node.children:
                node.children[ch] = TrieNode()
            node = node.children[ch]
        node.isWord = True

class Solution:
    def maxScoreWords(self, words: list[str], letters: list[str], score: list[int]) -> int:
        for i, word in enumerate(words):
            aw = list(word)
            aw.sort()
            words[i] = "".join(aw)
        print(words)
        # letters.sort()
        # n = len(letters)




