class OverheatPreventionController:
    def __init__(self, passive_cooling_capacity: float, active_cooling_capacity_per_core: float, core_ids: list[str]) -> None:
        self.passive_cooling_capacity=passive_cooling_capacity
        self.active_cooling_capacity_per_core=active_cooling_capacity_per_core
        self.core_ids=core_ids
        self.core_num=len(core_ids)
        self.record={}#实际的情况
        self.timestamp=float(0)
        self.pending=[]#全部pending记录
        self.active_cooling_cores=set()
        def createRecord():
            for i in range(len(self.core_ids)):
                self.record[self.core_ids[i]]={"status":"idle","temperature":20,"load":0}#status: idle/cooling/shutdown
        createRecord()
        self.init=self.record.deepcopy()#存一份储备
       
    def vibration_penalty(k): #k==num of cores that are actively cooling
        if k==0: return 0
        dp=[0]*(k+1)
        dp[0]=1
        dp[1]=1
        for i in range(2,k+1):
            dp[i]=dp[i-1]+dp[i-2]
        return sum(10 / dp[i] for i in range(1, k + 1))
    
    def SetCoreLoad(self, timestamp: float, core_id: str, load_watts: float) -> None:
        record={}#{core_id:{"status":"shutdown","load":load_watts,"timestamp":timestamp}}
        record[core_id]={}
        if self.record[core_id]["status"]=="shutdown":#restart
            record[core_id]["status"]="idle"#only valid if <50C next Tick
        record[core_id]["load"]=load_watts #set to 0 if >=50C next Tick
        record[core_id]["timestamp"]=timestamp
        self.pending.append(record)#[{core_id:{"status":"idle","load":load_watts,"timestamp":timestamp}}], 一个core_id可以有多条，其他值一样timestamp不一样也要记录

    def Tick(self, timestamp: float) -> list[str]:
        self.step=timestamp#step走到timestamp
        for k,v in self.record.items():#查找database
            if v["temperature"]>=80:
                v["load"]=0
                v["status"]="shutdown"
        #给self.pending按timestamp去重，留下self.step以前每个cpu最晚的时间record
        pending_tuples=[]
        for pend in self.pending:
            key=pend.keys()[0]#{core_id:{"status":"on","load":load_watts,"timestamp":timestamp}}
            value=pend[key]#{"status":"on","load":load_watts,"timestamp":timestamp}
            pending_tuples.append((key,value["timestamp"]))
        pending_tuples.sort(key=lambda x:(-x[1],x[0]))
        core_set=set()#看看该cpu在前面的记录里有没有出现过

        for tuple in pending_tuples:
            if tuple[0] in core_set:
                #从self.pending中挪走该记录🔥不知道怎样挪效率高
                pass

        #🔥这里假设self.pending是已经清理好不重复core的记录
        #开始执行变化
        for k,v in self.record.items():
            core_id=k
            if v["temperature"]<50 and self.record[core_id]["status"]=="idle": #可以restart,执行restart
               v["status"]="idle"#started
               #🔥v[core_id]["load"]=换成前面记录在self.pending里面的load_watts
            elif v["temperature"]>=50:
                #🔥v[core_id]["load"]=换成前面记录在self.pending里面的0
                #v={"status":"idle","temperature":20,"load":0}
                pass
            
            #temperature rate=dt/delta_load>0.5°C/s or temp>60C use active cooling,在self.active_cooling_cores里了已经
            
            #1. change temperature by Thermal Dynamics
            #0.02°C/s per watt
            #formula: temperature=delta_time x 0.02°C/s.w x delta_load(temp>=20)
            #passive: delta_load=min(2,self.passive_cooling_capacity/self.core_num)

            #2.Decides which cores should have active cooling engaged for the upcoming interval
            #temperature rate=dt/delta_load>0.5°C/s use active cooling
            penalty=self.vibration_penalty(len(self.active_cooling_cores))
            total_active_capacity=self.active_cooling_capacity_per_core*len(self.active_cooling_cores)
            new_passive_cooling_capacity=self.passive_cooling_capacity-penalty
            #Because engaging active cooling on a core increases the vibration penalty for everyone, it can in turn lift other cores' rates above 0.5°C/s and trigger their engagement as well within the same interval.
            #🔥上面这句话不知如何处理

        #与self.init对比看有哪些变化
        res=set()
        for k,v in self.init.items():
            if self.record[k]["status"]!=self.init[k]["status"]:
                res.add(k)

        return list(res)


#参考答案
class OverheatPreventionController:
    def __init__(self, passive_cooling_capacity: float, active_cooling_capacity_per_core: float, core_ids: list[str]) -> None:
        self.passive_capacity = passive_cooling_capacity
        self.active_capacity_per_core = active_cooling_capacity_per_core
        self.core_ids = core_ids
        
        # 初始化所有核心状态
        self.cores = {
            cid: {"temp": 20.0, "load": 0.0, "status": "idle"}
            for cid in core_ids
        }
        self.last_time = 0.0
        # 用字典记录 pending load，同一 core_id 多次设置会自动覆盖，只保留最后一次
        self.pending_loads = {}
        
        # 预计算斐波那契数列，用于震动惩罚计算 (1, 2, 3, 5, 8, 13...)
        self.fib = [1, 2]
        for _ in range(max(0, len(core_ids) - 2)):
            self.fib.append(self.fib[-1] + self.fib[-2])

    def vibration_penalty(self, k: int) -> float:
        """计算开启 k 个主动散热核心时的被动散热惩罚百分比"""
        if k == 0:
            return 0.0
        return sum(10.0 / self.fib[i] for i in range(k))

    def SetCoreLoad(self, timestamp: float, core_id: str, load_watts: float) -> None:
        # 直接存入/覆盖 pending_loads，在下一个 Tick 时再结算
        self.pending_loads[core_id] = load_watts

    def Tick(self, timestamp: float) -> list[str]:
        dt = timestamp - self.last_time #self.last_time初始为0
        self.last_time = timestamp
        
        # 记录本轮 Tick 之前的旧状态，用于最后对比
        old_status = {cid: self.cores[cid]["status"] for cid in self.core_ids}
        
        # ==========================================
        # 1. 热力学演算 (Thermal Dynamics)
        # ==========================================
        # 统计本轮起步前，开启了主动散热的核心数
        k_prev = sum(1 for cid in self.core_ids if self.cores[cid]["status"] == "cooling")
        penalty = self.vibration_penalty(k_prev)
        eff_passive = self.passive_capacity * (1.0 - penalty / 100.0)
        
        # 计算被动散热需求 (Demand = load + 2) 即使是 shutdown (load=0) 也有 2W 的需求
        demands = {cid: self.cores[cid]["load"] + 2.0 for cid in self.core_ids}
        total_demand = sum(demands.values())
        
        for cid in self.core_ids:
            core = self.cores[cid]
            # 分配被动散热
            if total_demand <= eff_passive:
                passive_alloc = demands[cid]
            else:
                passive_alloc = eff_passive * (demands[cid] / total_demand)
            
            # 分配主动散热
            active_alloc = self.active_capacity_per_core if core["status"] == "cooling" else 0.0
            
            # 计算净热量并更新温度 (最低 20.0°C)
            net_heat = core["load"] - passive_alloc - active_alloc
            core["temp"] = max(20.0, core["temp"] + dt * 0.02 * net_heat)

        # ==========================================
        # 2. 过热关机保护 (Shutdown)
        # ==========================================
        for cid in self.core_ids:
            if self.cores[cid]["temp"] >= 80.0:
                self.cores[cid]["load"] = 0.0
                self.cores[cid]["status"] = "shutdown"

        # ==========================================
        # 3. 结算待处理的 Load (Process pending loads)
        # ==========================================
        for cid, load in self.pending_loads.items():
            core = self.cores[cid]
            if core["status"] == "shutdown":
                # 重启尝试：温度必须严格低于 50°C
                if core["temp"] < 50.0:
                    core["load"] = load
                    core["status"] = "idle"  # 设为 idle，下一步马上重新评估是否需要 active cooling
            else:
                # 正常运行的核心直接更新负荷
                core["load"] = load
        self.pending_loads.clear()

        # ==========================================
        # 4. 评估下一阶段的主动散热需求 (Active Cooling)
        # ==========================================
        active_set = set()
        
        # 第一阶段：先加入所有超过 60°C 的核心
        for cid in self.core_ids:
            if self.cores[cid]["status"] != "shutdown" and self.cores[cid]["temp"] > 60.0:
                active_set.add(cid)

        # 第二阶段：连锁反应迭代，检查 temp rate > 0.5°C/s
        while True:
            k = len(active_set)
            pen = self.vibration_penalty(k)
            eff_pass = self.passive_capacity * (1.0 - pen / 100.0)
            
            demands = {cid: self.cores[cid]["load"] + 2.0 for cid in self.core_ids}
            tot_dem = sum(demands.values())
            
            changed = False
            for cid in self.core_ids:
                # 已关机或已在主动散热名单里的核跳过检查
                if cid in active_set or self.cores[cid]["status"] == "shutdown":
                    continue
                
                # 计算如果没有主动散热的情况下的升温速率
                if tot_dem <= eff_pass:
                    pass_alloc = demands[cid]
                else:
                    pass_alloc = eff_pass * (demands[cid] / tot_dem)
                
                net_heat = self.cores[cid]["load"] - pass_alloc
                rate = 0.02 * net_heat
                
                if rate > 0.5:
                    active_set.add(cid)
                    changed = True  # 有新核加入，引发连锁反应，需要重新循环计算
            
            # 当没有新的核被迫加入主动散热时，停止跌代
            if not changed:
                break
                
        # ==========================================
        # 应用新状态并输出变更
        # ==========================================
        res = []
        for cid in self.core_ids:
            if self.cores[cid]["status"] != "shutdown":
                self.cores[cid]["status"] = "cooling" if cid in active_set else "idle"
            
            if self.cores[cid]["status"] != old_status[cid]:
                res.append(f"{cid}={self.cores[cid]['status']}")
                
        return sorted(res)
