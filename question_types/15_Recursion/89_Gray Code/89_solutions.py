#20260624
class Solution:
    def grayCode(self, n: int) -> list[int]:
        if n == 1:
            return [0,1]
        
        # 获取 n-1 的格雷码
        prev = self.grayCode(n - 1)
        # 逆序遍历并加上最高位的 1
        return prev + [x + (1 << (n - 1)) for x in reversed(prev)]#reverse保证继承上一层的两个相邻变1，与上一层无缝衔接
    #1 << (n - 1)给最高位添1
    """
    n=1, [0,1]
    
    """
    