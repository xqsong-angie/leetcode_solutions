class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        state=[0]*(n+1)
        m=len(trust)

        #is there a person be trusted by n-1 people?
        for i in range(m):
            state[trust[i][1]]+=1

        assumed_judge=-1
        for i in range(1,n+1):
            if state[i]==n-1:
                assumed_judge=i
        #does this person trust anyone?
        for i in range(m):
            if trust[i][0]==assumed_judge:
                return -1
        return assumed_judge