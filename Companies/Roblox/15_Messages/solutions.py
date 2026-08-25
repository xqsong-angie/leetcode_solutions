def solution(members, events):
    # 提取 ID 的数字部分进行升序排序 (例如 "id42" -> 42)
    sorted_members = sorted(members, key=lambda x: int(x[2:]))
    
    # 记录每个用户的通知次数，初始为 0
    counts = {m: 0 for m in members}
    
    # 记录每个用户的离线到期时间 (解禁时间戳)，初始为 0 表示当前在线
    offline_until = {m: 0 for m in members}#HERE
    
    for event in events:
        action = event[0]
        time = int(event[1])
        data = event[2]
        
        if action == "OFFLINE":
            user_id = data
            # 用户从 time 开始离线，将在 time + 60 恢复在线
            offline_until[user_id] = time + 60
            
        elif action == "MESSAGE":
            tokens = data.split()
            mentioned_in_this_msg = set()
            
            for token in tokens:
                if token == "ALL":
                    # ALL 提及所有用户
                    for m in members:
                        mentioned_in_this_msg.add(m)
                        
                elif token == "HERE":
                    # HERE 只提及当前在线的用户 (当前时间 >= 离线到期时间)
                    for m in members:
                        if time >= offline_until[m]:
                            mentioned_in_this_msg.add(m)
                            
                else:
                    # 单个 ID 提及 (例如 "id158")
                    if token in counts:
                        mentioned_in_this_msg.add(token)
            
            # 对本条消息中提及的所有用户增加 1 次计数 (set 保证了单条消息内自动去重)
            for m in mentioned_in_this_msg:
                counts[m] += 1
                
    # 按照 ID 数字大小升序构建结果数组
    return [f"{m}={counts[m]}" for m in sorted_members]