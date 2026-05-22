class Trie:
    def __init__(self):
        self.root={}

    def insert(self, word: str) -> None:
        node=self.root
        for c in word:
            if c not in node:
                node[c]={}
            node=node[c]
        node['#']='#'


    def search(self, word: str) -> bool:
        node=self.root
        for c in word:
            if c in node:
                node=node[c]
            else:
                return False
        return '#' in node and node['#']=='#'

    def startsWith(self, prefix: str) -> bool:
        node=self.root
        for c in prefix:
            if c in node:
                node=node[c]
            else:
                return False
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)