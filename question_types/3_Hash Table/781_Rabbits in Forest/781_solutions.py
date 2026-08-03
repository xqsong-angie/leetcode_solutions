#20260803
class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        for i in range(len(answers)):
            answers[i]+=1
        cnt=Counter(answers)
        min_cnt=0
        for k,v in cnt.items():
            min_cnt+=ceil(v/k)*k
        return min_cnt