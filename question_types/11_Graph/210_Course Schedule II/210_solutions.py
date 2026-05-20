class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        #1.统计入度
        indegree=[0 for i in range(numCourses)]
        for a,b in prerequisites:
            indegree[a]+=1
        #2.找入度为零的当根
        queue=[]
        visited=set()
        for i in range(numCourses):
            if indegree[i]==0:
                flag=True
                visited.add(i)
                queue.append(i) 
        #3.bfs
        res=[]
        while queue:
            cur=queue.pop(0)
            res.append(cur)
            for a,b in prerequisites:
                if b==cur:
                    indegree[a]-=1
                    flag=False
                if a not in visited and indegree[a]==0:
                    flag=True
                    visited.add(a)
                    queue.append(a)
        if len(res)==numCourses:
            return res
        else:
            return []




