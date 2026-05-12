class Solution:

    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        n=len(people)
        #先定身高（从大到小）,再定个数(从小到大)
        people=sorted(people,key=lambda x:(-x[0],x[1]))
        for i in range(n):
            if people[i][1]<i:
                temp=people[i]
                for j in range(i-1,temp[1]-1,-1):
                    people[j+1]=people[j]
                people[temp[1]]=temp
        return people
        