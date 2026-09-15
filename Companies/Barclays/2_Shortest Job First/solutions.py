def solution(req_time,duration):
    n_task=len(duration)
    mytuple=[x for x in zip(duration,req_time)]
    mytuple.sort(key=lambda x: (x[1],x[0]))
    res=0
    time=0
    for i in range(len(mytuple)):
        if i==0:
            res+=0
            time+=mytuple[i][0]
        elif time>mytuple[i][1]:
            res+=time-mytuple[i][1]
        else:
            res+=0

    return round(res / n_task, 2)


import heapq

def solution(req_time, duration):
    n_task = len(duration)
    # 将任务组合为: (请求时间, 执行时长, 原始序号)
    tasks = [(req_time[i], duration[i], i) for i in range(n_task)]
    # 按请求时间升序排序，方便后续按时间推进装载任务
    tasks.sort(key=lambda x: x[0])#Python 的排序是稳定排序 是指按照原相对顺序
    
    current_time = 0
    total_waiting_time = 0
    task_idx = 0
    
    # 最小堆（就绪队列）：按 (duration, req_time) 堆排序
    ready_queue = []
    
    completed_count = 0
    while completed_count < n_task:
        # 1. 将所有在 current_time 及之前到达的任务放入就绪队列
        while task_idx < n_task and tasks[task_idx][0] <= current_time:
            req, dur, _ = tasks[task_idx]
            # 堆以 tuple(dur, req) 进行排序：duration 小的优先；若相同则 req 小的优先
            heapq.heappush(ready_queue, (dur, req))
            task_idx += 1
            
        # 2. 如果就绪队列非空，弹出最短的任务执行
        if ready_queue:
            dur, req = heapq.heappop(ready_queue)
            # 等待时间 = 开始执行时间 - 请求时间
            total_waiting_time += current_time - req
            # 更新系统当前时间
            current_time += dur
            completed_count += 1
        else:
            # 如果就绪队列为空，说明系统处于空闲状态，直接跳到下一个任务的到达时间
            current_time = tasks[task_idx][0]
            
    avg_waiting_time = total_waiting_time / n_task
    # 保留两位小数返回字符串格式
    return f"{avg_waiting_time:.2f}"
        
