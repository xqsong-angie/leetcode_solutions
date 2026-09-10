#20250620
class Solution:
    def isHappy(self, n: int) -> bool:
        #how to end an "endless" loop: https://www.youtube.com/watch?v=8wDuRgQ2dvw
        sum_set=set()
        mysum=0
        n_str=str(n)
        n_list=list(n_str)
        while True:
            mysum=0
            for i in range(len(n_list)):
                mysum+=int(n_list[i])**2
            if mysum in sum_set and mysum!=1:
                return False
            elif mysum in sum_set and mysum==1:
                return True
            sum_set.add(mysum)
            n_str=str(mysum)
            n_list=list(n_str)

