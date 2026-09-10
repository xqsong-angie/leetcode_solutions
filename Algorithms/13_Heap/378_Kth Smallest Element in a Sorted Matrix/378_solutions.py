class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        #利用最小堆做多路归并（K-way Merge）
        n = len(matrix)
        # (value, row, col)
        heap = [(matrix[i][0], i, 0) for i in range(n)]#先放第一列
        heapq.heapify(heap)  # O(n)
    
        for _ in range(k):
            val, row, col = heapq.heappop(heap)
            if col + 1 < n:
                heapq.heappush(heap, (matrix[row][col+1], row, col+1))#某一行有空位了，拿第二顺位补进去
        
        return val

#20260724 看了一遍
