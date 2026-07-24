class Trie:
    def __init__(self):
        self.root={}

    def insert(self, word: str) -> None:
        node=self.root
        for c in word:
            if c not in node:
                node[c]={}
            node=node[c]
        node['#']='#' #end


    def search(self, word: str) -> bool:
        node=self.root
        for c in word:
            if c in node:
                node=node[c]
            else:
                return False
        return '#' in node and node['#']=='#'#只要'#' in node就够了，不需要后面那个

    def startsWith(self, prefix: str) -> bool:
        node=self.root
        for c in prefix:
            if c in node:
                node=node[c]
            else:
                return False
        return True#不用到底，只要prefix过完了还没return False,就是True了


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)

#20260724 看了一遍