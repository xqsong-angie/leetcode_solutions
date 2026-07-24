class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph=defaultdict(list)
        for u,v,w in times:
            graph[u].append((v,w))#邻居及权重
        dist=[float('inf')]*(n+1)
        dist[k]=0#k是src
        heap=[(0,k)]#src先入堆

        while heap:
            d,node=heapq.heappop(heap)#
            if d>dist[node]: #这个过期了，跳过
                continue
            for neighbor,weight in graph[node]:#🔥d==dist[node]
                if dist[node]+weight<dist[neighbor]:#dist[node]+weight是从node到neigbor,dist[neighbor]是原来自己的
                    dist[neighbor]=dist[node]+weight#🔥d<dist[node]的情况不可能存在，因为此时已经把新d赋值给了dist[node]
                    heapq.heappush(heap,(dist[neighbor],neighbor))#要不断找最小的那个点
        ans=max(dist[1:])#节点从1开始，0的inf不要
        return ans if ans!=float('inf') else -1
        
#20260723 看了一遍



        
