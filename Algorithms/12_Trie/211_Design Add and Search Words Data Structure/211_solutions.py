class WordDictionary:

    def __init__(self):
        self.root={}

    def addWord(self, word: str) -> None:
        node=self.root
        for c in word:
            if c not in node:
                node[c]={}
            node=node[c]
        if '#' not in node:
            node['#']='#'

    def search(self, word: str) -> bool:
        def dfs(index, node):
            if index==len(word):
                return '#' in node
            else:
                if word[index]==".":
                    for child in node:#每一条路都没返回True,说明没找到
                        if child != '#':
                            if dfs(index+1,node[child]):
                                return True
                    return False

                elif word[index] in node:#单个的
                    return dfs(index+1, node[word[index]])#直接再往下就行了
                else:
                    return False
        return dfs(0, self.root)

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)

#🔥20260707: 不会做，看了一遍solution
#20260724 看了一遍