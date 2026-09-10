#20260726
class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n<=0:
            return False
        elif 0<n<1:
            return self.isPowerOfThree(n*3)
        elif n==1:
            return True
        elif n%3!=0:
            return False
        else:
            return self.isPowerOfThree(n/3)