class Solution:

    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        n=len(people)
        #先定身高（从大到小）,再定个数(从小到大)，因为小个子不会影响大个子的相对位置
        people=sorted(people,key=lambda x:(-x[0],x[1]))
        for i in range(n):#i是排的位置
            if people[i][1]<i:#就说明要挪动
                temp=people[i]
                for j in range(i-1,temp[1]-1,-1): #temp不可能到temp[1]以前的位置去
                    people[j+1]=people[j]
                people[temp[1]]=temp
        return people
        
#20260712 看了一遍