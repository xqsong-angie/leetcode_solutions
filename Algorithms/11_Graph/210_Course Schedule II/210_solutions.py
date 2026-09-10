class Solution:
    #拓扑排序的最终输出结果永远是一维的线性序列，如果有并列的，并列位置随机（会有多个拓扑序出来）
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        #1.统计入度
        indegree=[0 for i in range(numCourses)]
        for a,b in prerequisites:
            indegree[a]+=1

        #2.找入度为零的当根（第一个要上的课）
        queue=[]
        visited=set()
        for i in range(numCourses):
            if indegree[i]==0:
                visited.add(i)
                queue.append(i) 
        #3.bfs
        res=[]
        while queue:
            cur=queue.pop(0)
            res.append(cur)
            for a,b in prerequisites:
                if b==cur:
                    indegree[a]-=1#谁先减到0，谁就是下一个
                if a not in visited and indegree[a]==0:
                    visited.add(a)
                    queue.append(a)
        if len(res)==numCourses:
            return res
        else:
            return []

#20260723 看了一遍


