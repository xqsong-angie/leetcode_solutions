class Solution:
    def candy(self, ratings: List[int]) -> int:
        n=len(ratings)
        candies=[1]*n
        if n!=1:
            #right 负责递增 【1，2，3，4，2，2，2，1】
            for i in range(1,n):
                if ratings[i]>ratings[i-1] and candies[i]<=candies[i-1]:
                    candies[i]=candies[i-1]+1
                elif ratings[i]<ratings[i-1] and candies[i]>=candies[i-1]:
                    candies[i-1]=candies[i]+1
            #left [1, 3, 4, 5, 4, 3, 2, 1] 负责递减 [1, 2, 3, 5, 4, 3, 2, 1]
            for i in range(n-1,0,-1):
                if ratings[i-1]<ratings[i] and candies[i-1]>=candies[i]:
                    candies[i]=candies[i-1]+1
                elif ratings[i-1]>ratings[i] and candies[i-1]<=candies[i]:
                    candies[i-1]=candies[i]+1

        return sum(candies)
    
#20260712 看了一遍，注意双向