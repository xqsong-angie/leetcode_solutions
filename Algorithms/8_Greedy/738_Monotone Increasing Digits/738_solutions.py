class Solution:
    def monotoneIncreasingDigits(self, n: int) -> int:
        if n<10:
            return n
        else:
            mylist=list(str(n))
            for i in range(len(mylist)-2,-1,-1):
                if int(mylist[i])>int(mylist[i+1]):
                    mylist[i]=str(int(mylist[i])-1)
                    for j in range(i+1,len(mylist)):
                        mylist[j]="9"
                    

            return int("".join(mylist))


        
