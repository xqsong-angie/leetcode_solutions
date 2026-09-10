class MapSum:

    def __init__(self):
        self.root={}

    def insert(self, key: str, val: int) -> None:
        node=self.root
        for c in key:
            if c not in node:
                node[c]={}
            node=node[c]
        node["#"]=val

    def sum(self, prefix: str) -> int:
        def dfs(node):
            mysum=0
            for c in node:
                if c=="#":
                    mysum+=node["#"]
                else:
                    mysum+=dfs(node[c])
            return mysum

        node=self.root
        for p in prefix:
            if p in node:
                node=node[p]
            else:
                return 0

        return dfs(node)    
# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)