class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        balance=[0,0,0]
        n=len(bills)
        for i in range(n):
            if bills[i]==5:
                balance[2]+=1
            elif bills[i]==10:
                balance[1]+=1
            else:#20
                balance[0]+=1
            
            #change
            change=bills[i]-5
            if change==15:
                if balance[1]>0 and balance[2]>0:
                    balance[1]-=1
                    balance[2]-=1
                elif balance[2]>=3:
                    balance[2]-=3
                else:
                    return False
            elif change==5:
                if balance[2]>0:
                    balance[2]-=1
                else:
                    return False

        return True