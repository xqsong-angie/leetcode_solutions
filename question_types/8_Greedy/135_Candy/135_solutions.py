class Solution:
    def candy(self, ratings: List[int]) -> int:
        n=len(ratings)
        candies=[1]*n
        if n!=1:
            #right
            for i in range(1,n):
                if ratings[i]>ratings[i-1] and candies[i]<=candies[i-1]:
                    candies[i]=candies[i-1]+1
                elif ratings[i]<ratings[i-1] and candies[i]>=candies[i-1]:
                    candies[i-1]=candies[i]+1
            #left
            for i in range(n-1,0,-1):
                if ratings[i-1]<ratings[i] and candies[i-1]>=candies[i]:
                    candies[i]=candies[i-1]+1
                elif ratings[i-1]>ratings[i] and candies[i-1]<=candies[i]:
                    candies[i-1]=candies[i]+1

        return sum(candies)