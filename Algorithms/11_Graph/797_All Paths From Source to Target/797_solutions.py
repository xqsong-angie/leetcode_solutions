class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        self.path=[]
        self.res=[]
        self.visited=set()
        n=len(graph)
        def dfs(start,n):
            self.visited.add(start)
            self.path.append(start)
            if start<n-1:
                for node in graph[start]:
                        if node not in self.visited:
                            self.visited.add(node)
                            dfs(node,n)
            else:
                self.res.append(list(self.path))
                self.visited=set()
            self.path.pop() #回溯

        dfs(0,n)
        return self.res
                   