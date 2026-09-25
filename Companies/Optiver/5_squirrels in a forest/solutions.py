from collections import defaultdict
class SquirrelResearch:
    def __init__(self, locations: dict[str, int]) -> None:
        self.locations=locations# all available hiding locations {loc_id1:levels1,loc_id2:levels2,...}
        self.hidden_nuts=defaultdict(list)#{location_id:[{"timestamp":timestamp,"nut_weight":nut_weight,"time_to_expire":time_to_expire,"expired":False}]}
        self.hidden_nut_ids=set()
        #get fib sequence
        max_levels=0
        for _,v in self.locations.items():
            max_levels=max(max_levels,v)
        self.fib=[0]*max_levels#🔥fib起始项错误
        self.fib[0]=self.fib[1]=1
        for i in range(2,max_levels):
            self.fib[i]=self.fib[i-1]+self.fib[i-2]
        #initialize number of current nuts stored in every location
        self.location_nuts=defaultdict(int)
        self.prev=None

        
    def HideNut(self, timestamp: float, location_id: str, nut_id: str, nut_weight: float, time_to_expire: float) -> bool:
        if nut_id in self.hidden_nut_ids or location_id not in self.locations.keys() or self.location_nuts[location_id]==sum(self.fib[:self.locations[location_id]]):#full
            return False
        self.hidden_nut_ids.add(nut_id)
        insert={"nut_id":nut_id,"timestamp":timestamp,"nut_weight":nut_weight,"time_to_expire":time_to_expire,"expired":False}
        if self.timestamp>=timestamp+time_to_expire:
            insert["expired"]=True       

        #determine which level the nut belongs to
        self.location_nuts[location_id]+=1
        fib_sum=0
        level=1
        for i in range(len(self.fib)):
            fib_sum+=self.fib[i]
            if fib_sum>=self.location_nuts[location_id]:
                level=i
        insert["level"]=level
        self.hidden_nuts[location_id].append(insert)

        return True

    def RetrieveNuts(self, timestamp: float, location_id: str, max_squirrel_capacity_in_nuts: int) -> list[str]:
        if location_id not in self.locations.keys() or self.location_nuts[location_id]==0:#empty
            return []
        retrieved_nuts=[]#[nut_id1,nut_id2,nut_id3,...]
        cur_loc=location_id
        levels=self.locations[cur_loc]
        #get all nut_ids belong to cur_loc
        all_nut_ids=self.hidden_nuts[location_id]#[{"nut_id":nut_id,"timestamp":timestamp,"nut_weight":nut_weight,"time_to_expire":time_to_expire,"expired":False,"level":level}]
        #sort by level
        all_nut_ids.sort(key=lambda x:(-x["level"],-x["nut_weight"],x["nut_id"]))
        total_nuts=self.location_nuts[cur_loc]
        max_squirrel_capacity_in_nuts
        #retrieve nuts
        for i in range(len(all_nut_ids)):
            cur_nut=all_nut_ids[i]#{"nut_id":nut_id,"timestamp":timestamp,"nut_weight":nut_weight,"time_to_expire":time_to_expire,"expired":False,"level":level}
            cur_level=cur_nut["level"]
            #check if the nut expired
            if timestamp>=cur_nut["timestamp"]+cur_nut["time_to_expire"]:
                all_nut_ids.remove(cur_nut)#🔥for i in range(len(all_nut_ids))搭配all_nut_ids.remove(...) 会直接导致数组下标越界,因为len(all_nut_ids)没有动态变化
                self.location_nuts[cur_loc]-=1
                total_nuts-=1
                self.hidden_nut_ids.remove(cur_loc["nut_id"])

            #check if current level has less than half of capacity
            elif total_nuts-sum(self.fib[:cur_level-1])<0.5*self.fib[cur_level-1]:
                #can access to the next level
                if self.prev==None:
                    self.prev=cur_nut
                else:#说明上一层的已经保存了
                    if self.prev["nut_weight"]>=cur_nut["nut_weight"]:
                        #松鼠要拿走self.prev
                        retrieved_nuts.append(self.prev["nut_id"])
                        #清除该id
                        all_nut_ids.remove(cur_nut)
                        self.location_nuts[cur_loc]-=1
                        total_nuts-=1
                        self.hidden_nut_ids.remove(cur_loc["nut_id"])
            #🔥没有写出下落机制，坚果要分层管理
        return retrieved_nuts

#参考答案
class SquirrelResearch:
    def __init__(self, locations: dict[str, int]) -> None:
        # locations: {loc_id: levels}
        self.locations = locations
        
        # 生成斐波那契数列: 1, 2, 3, 5, 8, 13, ...
        # max_levels 上限为 32
        self.fib = [1, 2]#🔥从一开始就设定好从第三位开始的最初两个数
        while len(self.fib) < 40:
            self.fib.append(self.fib[-1] + self.fib[-2])
        # 截取从第 3 位开始的容量序列: level 0 -> fib[0]=1, level 1 -> fib[1]=2, ...
        
        # 记录全图已存放的 nut_id
        self.global_nut_ids = set()
        
        # 每个 location 的存储结构: 
        # self.storage[loc_id] = [ [nut1, nut2...], [nut...], ... ] 
        # 外层列表索引 0 代表最深层 (Level 1)
        self.storage = {loc_id: [[] for _ in range(num_levels)] for loc_id, num_levels in locations.items()}

    def _get_level_capacity(self, level_idx: int) -> int:
        # level_idx: 0 -> 1, 1 -> 2, 2 -> 3, 3 -> 5...
        return self.fib[level_idx]

    def HideNut(self, timestamp: float, location_id: str, nut_id: str, nut_weight: float, time_to_expire: float) -> bool:
        # 1. 基础异常校验
        if location_id not in self.locations:
            return False
        if nut_id in self.global_nut_ids:
            return False

        loc_levels = self.storage[location_id]
        
        # 2. 从最深层 (0) 向上寻找第一个未满的层级
        target_level = -1
        for level_idx in range(len(loc_levels)):
            if len(loc_levels[level_idx]) < self._get_level_capacity(level_idx):
                target_level = level_idx
                break
                
        # 整个 location 已满
        if target_level == -1:
            return False

        # 3. 成功储存坚果
        nut_obj = {
            "nut_id": nut_id,
            "weight": nut_weight,
            "timestamp": timestamp,
            "time_to_expire": time_to_expire
        }
        loc_levels[target_level].append(nut_obj)
        self.global_nut_ids.add(nut_id)
        return True

    def RetrieveNuts(self, timestamp: float, location_id: str, max_squirrel_capacity_in_nuts: int) -> list[str]:
        if location_id not in self.locations:
            return []

        loc_levels = self.storage[location_id]
        
        # 检查 location 是否为空
        total_nuts = sum(len(lvl) for lvl in loc_levels)
        if total_nuts == 0:
            return []

        retrieved_nut_ids = []

        while len(retrieved_nut_ids) < max_squirrel_capacity_in_nuts:
            # 1. 重新找到当前有坚果的最顶层 (upmost level)
            upmost_level = -1
            for l_idx in range(len(loc_levels) - 1, -1, -1):
                if len(loc_levels[l_idx]) > 0:
                    upmost_level = l_idx
                    break

            # 如果所有层都空了，结束取出
            if upmost_level == -1:
                break

            # 2. 判断当前可取坚果的候选层（Upmost level + 可能的 Next level）
            candidate_levels = [upmost_level]
            
            # 检查 upmost level 是否占用小于 50% 容量
            upmost_capacity = self._get_level_capacity(upmost_level)
            if len(loc_levels[upmost_level]) < 0.5 * upmost_capacity:
                # 下一层 (upmost_level - 1) 也变为可触及
                if upmost_level - 1 >= 0 and len(loc_levels[upmost_level - 1]) > 0:
                    candidate_levels.append(upmost_level - 1)

            # 3. 从候选层中收集所有可选坚果并排序
            candidates = []
            for lvl_idx in candidate_levels:
                for nut in loc_levels[lvl_idx]:
                    candidates.append((nut, lvl_idx))

            if not candidates:
                break

            # 排序规则:
            # - Heavier nuts first (-weight)
            # - Tie on weight: smallest nut_id alphabetically (nut_id)
            candidates.sort(key=lambda item: (-item[0]["weight"], item[0]["nut_id"]))
            
            # 选中最佳坚果
            chosen_nut, chosen_level = candidates[0]

            # 4. 从该层移除被选中的坚果
            loc_levels[chosen_level].remove(chosen_nut)
            self.global_nut_ids.remove(chosen_nut["nut_id"])

            # 5. 触发物理下落机制 (Fall down physics)
            # 如果拿走坚果的层不是当前最顶层 (chosen_level < upmost_level)
            # 上一层 (chosen_level + 1) 中最轻的坚果下落填补该层
            curr_fill_level = chosen_level
            while curr_fill_level < upmost_level:
                above_level = curr_fill_level + 1
                if len(loc_levels[above_level]) > 0:
                    # 找到上面一层最轻的坚果 (Lightest -> 权重最小，ID 字典序最小)
                    lightest_nut = min(loc_levels[above_level], key=lambda x: (x["weight"], x["nut_id"]))
                    # 移动到下一层
                    loc_levels[above_level].remove(lightest_nut)
                    loc_levels[curr_fill_level].append(lightest_nut)
                    curr_fill_level += 1
                else:
                    break

            # 6. 判断该坚果是否过期 (Immediate Discard check)
            is_expired = timestamp > (chosen_nut["timestamp"] + chosen_nut["time_to_expire"])
            
            if not is_expired:
                retrieved_nut_ids.append(chosen_nut["nut_id"])

        return retrieved_nut_ids