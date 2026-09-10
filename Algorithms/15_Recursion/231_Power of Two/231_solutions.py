#20260726
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n<=0:
            return False
        elif 0<n<1:
            return self.isPowerOfTwo(n*2)
        elif n==1:
            return True
        elif n%2!=0:
            return False
        else:
            return self.isPowerOfTwo(n/2)