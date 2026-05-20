class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph=defaultdict(list)
        for u,v,w in times:
            graph[u].append((v,w))
        dist=[float('inf')]*(n+1)
        dist[k]=0
        heap=[(0,k)]#src先入堆

        while heap:
            d,node=heapq.heappop(heap)
            if d>dist[node]: #不要更新
                continue
            for neighbor,weight in graph[node]:
                if dist[node]+weight<dist[neighbor]:#dist[node]+weight是从node到neigbor,dist[neighbor]是原来自己的
                    dist[neighbor]=dist[node]+weight
                    heapq.heappush(heap,(dist[neighbor],neighbor))#要不断找最小的那个点
        ans=max(dist[1:])
        return ans if ans!=float('inf') else -1
        




        
