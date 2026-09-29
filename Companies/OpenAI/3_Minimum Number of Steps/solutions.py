from collections import deque
#参考答案
def minSteps(nums: list[int], start: int, target: int, N: int) -> int:
    if start == target:
        return 0
    
    # 优化1：对 nums 元素对 N 取模并去重
    transitions = {x % N for x in nums} 
    
    # BFS 队列，存储 (当前数值, 当前步数)
    queue = deque([(start, 0)])
    visited = [False] * N
    visited[start] = True
    
    while queue:
        curr, steps = queue.popleft()
        
        for step_val in transitions:
            nxt = (curr + step_val) % N
            
            if nxt == target:
                return steps + 1
            
            if not visited[nxt]:
                visited[nxt] = True
                queue.append((nxt, steps + 1))
                
    return -1