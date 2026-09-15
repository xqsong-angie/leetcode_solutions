from collections import defaultdict
class Solution:
    def solution(self,efficiency,ids,fire_resign_list):
        """
        efficiency:[1,2,3,4,5],
        ids:[1,2,1,1,2]
        fire_resign_list:[(3,2),(2,0)]
        """
        res=sum(efficiency)
        mymap=defaultdict(list)
        for i in range(len(ids)):
            mymap[ids[i]].append(efficiency[i])

        for k,v in mymap:
            v.sort(reversed=True)

        for f in fire_resign_list:
            id=ids[f[0]-1]
            if id==0:
                continue
            else:
                for i in range(f[1]):#这里无法把idFire的那一个过滤出去
                    mymap[id].pop()
                ids[f[0]-1]=0


def get_reputation(efficiencies, team_ids, fire_resign_list):
    current_reputation = sum(efficiencies)
    
    # 按照 team_id 分组存储效率（保持原始输入顺序，不排序）
    teams = defaultdict(list)
    for i in range(len(efficiencies)):
        teams[team_ids[i]].append(efficiencies[i])

    res = []

    for id_fire, num_resign in fire_resign_list:
        emp_idx = id_fire - 1 #把1-based改成0-based
        fire_eff = efficiencies[emp_idx]
        tid = team_ids[emp_idx]
        team_list = teams[tid]

        # 1. 移除被解雇的员工
        team_list.remove(fire_eff)#列表移除任意元素的函数
        current_reputation -= fire_eff

        # 2. 依次找到并移除剩余员工中效率最低的 K 个人
        for _ in range(min(num_resign, len(team_list))):#🔥若不足k个，删掉全部
            min_eff = min(team_list)
            team_list.remove(min_eff)
            current_reputation -= min_eff

        res.append(current_reputation)

    return res