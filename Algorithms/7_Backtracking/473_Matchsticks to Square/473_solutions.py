#20260703
class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        total=sum(matchsticks)
        if total % 4 !=0:#说明肯定分不成四条边
            return False
        target=total//4#每条边目标大小
        matchsticks.sort(reverse=True) #🔥长火柴尽早触发回溯
        sides=[0,0,0,0] #初始化空桶分别记录四条边当前长度
        def backtracking(pt):
            if pt==len(matchsticks):#说明所有火柴都用到了
                return True
            for i in range(4):#试当前火柴放入每条边
                if sides[i]+matchsticks[pt]<=target:
                    sides[i]+=matchsticks[pt]
                    if backtracking(pt+1):
                        return True
                    sides[i]-=matchsticks[pt]#回溯
                if sides[i]==0:#轻量剪枝，0是最核心的痛点O(1)，比把所有相等的剪枝更轻量O（N)
                    break
            return False
        return backtracking(0)
    
#20260711 看了一遍