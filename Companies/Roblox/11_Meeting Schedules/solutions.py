#20260823
class Solution:
    def solution(self, schedules: list[list[list[int]]], length: int) -> int:
        DAY_END = 24 * 60  # 1440 分钟
        
        # 1. 收集所有员工的所有会议区间
        all_meetings = []
        for emp in schedules:
            for meeting in emp:
                all_meetings.append(meeting)
                
        # 如果没有任何会议，直接从第 0 分钟开始
        if not all_meetings:
            return 0 if length <= DAY_END else -1
            
        # 2. 按 startTime 升序排序
        all_meetings.sort(key=lambda x: x[0])
        
        # 3. 合并有重叠的区间
        merged = []
        for start, end in all_meetings:
            if not merged or merged[-1][1] < start:#上一个end比当前start要早
                merged.append([start, end])
            else:
                merged[-1][1] = max(merged[-1][1], end)#否则要合并
                
        # 4. 在合并后的繁忙区间之间寻找空隙
        curr_time = 0
        for start, end in merged:
            # 检查从 curr_time 到 start 是否有足够空间
            if start - curr_time >= length:
                return curr_time
            # 如果没有，更新可能的最早开始时间
            curr_time = max(curr_time, end)
            
        # 5. 检查一天剩下的时间（从最后一个会议结束到 1440 分钟）🔥所有会议之间都没有空位，看距离一天结束还有没有
        if DAY_END - curr_time >= length:
            return curr_time
            
        return -1