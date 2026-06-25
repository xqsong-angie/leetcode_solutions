#20260624
#错（超时）
class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n==1:
            return x
        elif n==-1:
            return 1/x
        else:
            return self.myPow(x,n//2)*self.myPow(x,n-n//2) #虽然有拆分，但左右还是分别计算了，计算量没少
#对
class Solution:
    def myPow(self, x: float, n: int) -> float:
        # 1. 必须处理 n = 0 的边界情况,即使n没有0，也会在递归后续某一步遇到
        if n == 0: 
            return 1.0
        
        # 2. 如果是负数幂，先转换为正数算，最后取倒数（在 Python 中，整除运算符 // 是向下取整，-1//2还是-1，会无限递归下去）
        if n < 0:
            return 1 / self.myPow(x, -n)
        
        # 3. 核心：只递归一次！把结果存到变量里
        half = self.myPow(x, n // 2)
        
        # 4. 根据奇偶性决定最终结果
        if n % 2 == 0:
            return half * half       # 偶数次方：(x^(n/2))^2
        else:
            return half * half * x   # 奇数次方：(x^(n/2))^2 * x