class TrieNode:
    def __init__(self):
        self.child = {}
        self.fin = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for w in word:
            if w not in node.child:
                node.child[w] = TrieNode()
            node = node.child[w]
        node.fin = True

a = Trie()
a.insert("abcd")
print(a.root.child)
