#20260703
class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        total=sum(matchsticks)
        if total % 4 !=0:
            return False
        target=total//4
        matchsticks.sort(reverse=True) #长火柴尽早触发回溯
        sides=[0,0,0,0] #初始化空桶分别记录四条边当前长度
        def backtracking(pt):
            if pt==len(matchsticks):#说明所有火柴都用到了
                return True
            for i in range(4):
                if sides[i]+matchsticks[pt]<=target:
                    sides[i]+=matchsticks[pt]
                    if backtracking(pt+1):
                        return True
                    sides[i]-=matchsticks[pt]
                if sides[i]==0:
                    break
            return False
        return backtracking(0)